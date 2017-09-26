
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-25

@author: zhoucuilian
"""
import pandas as pd
import numpy as np
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV

import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 12, 4


def modelfit(alg,train_x, train_y, test_x, test_y, useTrainCV=True, cv_folds=5, early_stopping_rounds=50):

    if useTrainCV:
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(train_x, label=train_y)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds,
                    metrics='auc', early_stopping_rounds=early_stopping_rounds)
        print cvresult.shape[0]
        alg.set_params(n_estimators=cvresult.shape[0])

    #Fit the algorithm on the data
    alg.fit(train_x, train_y,eval_metric='auc')

    #Predict training set:
    dtrain_predictions = alg.predict(train_x)
    dtrain_predprob = alg.predict_proba(train_x)[:,1]

    #
    # #Print model report:
    print "\nModel Report"
    print "Accuracy(Train) : %.4g" % metrics.accuracy_score(train_y, dtrain_predictions)
    print "AUC Score (Train): %f" % metrics.roc_auc_score(train_y, dtrain_predprob)

    # #     Predict on testing data:
    dtest_predictions = alg.predict(test_x)
    dtest_predprob = alg.predict_proba(test_x)[:,1]
    print "Accuracy(Test) : %.4g" % metrics.accuracy_score(test_y, dtest_predictions)
    print 'AUC Score (Test): %f' % metrics.roc_auc_score(test_y,dtest_predprob)



    feat_imp = pd.Series(alg.get_booster().get_fscore()).sort_values(ascending=False)
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')

def run_xgboost(train_x, train_y, test_x, test_y):

    xgb1 = XGBClassifier(
            learning_rate =0.1,
            n_estimators=600,
            max_depth=3,
            min_child_weight=1,
            gamma=0,
            subsample=0.8,
            colsample_bytree=0.8,
            objective= 'binary:logistic',
            nthread=4,
            scale_pos_weight=1,
            seed=27)
   # modelfit(xgb1,train_x,train_y,test_x,test_y)


