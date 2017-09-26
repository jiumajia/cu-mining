#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""

import time

from sklearn import svm
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import xgboost as xgb


def SVM(tran_x, train_y, test_x, test_y):
    gamma_2d_range = [x * 0.01 for x in range(2, 30)]
    C_2d_range = [x for x in range(2, 30)]
    kernel_function = ['rbf', 'poly', 'sigmoid']

    # step1:training svm,save optimal parameter
    start = time.clock()
    iter_num = 0
    accuracy = 0
    for svm_k in kernel_function:
        for svm_c in C_2d_range:
            for svm_g in gamma_2d_range:
                iter_num += 1
                cfr = svm.SVC(kernel=svm_k, C=svm_c, gamma=svm_g)
                cfr.fit(tran_x, train_y)
                p_out = cfr.predict(test_x)
                accuracy_t = accuracy_score(test_y, p_out)
                if (accuracy < accuracy_t):
                    accuracy = accuracy_t
                    params = cfr.get_params()

    end = time.clock()
    print 'svm --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params



def RandomForest(tran_x, train_y, test_x, test_y):
    accuracy = 0
    n_estimators_range = [x for x in range(10, 100)]
    criterion = ['gini', 'entropy']

    # step1:training svm,save optimal parameter
    iter_num = 0
    start = time.clock()
    for c in criterion:
        for n in n_estimators_range:
            iter_num += 1
            cfr = RandomForestClassifier(n_estimators=n, criterion=c)
            cfr.fit(tran_x, train_y)
            p_out = cfr.predict(test_x)
            accuracy_t = accuracy_score(test_y, p_out)
            if (accuracy < accuracy_t):
                accuracy = accuracy_t
                params = cfr.get_params()

    end = time.clock()
    print 'RandomForest --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params


def Linear(tran_x, train_y, test_x, test_y):
    solver = ['liblinear', 'newton-cg', 'sag', 'lbfgs']
    # step1:training svm,save optimal parameter
    iter_num = 0
    start = time.clock()
    accuracy = 0
    for s in solver:
        iter_num += 1
        cfr = LogisticRegression(solver=s)
        cfr.fit(tran_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(test_y, p_out)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
            out = p_out
    end = time.clock()
    print 'LR --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    print len(out)
    return out


def DecisionTree(tran_x, train_y, test_x, test_y):
    accuracy = 0
    criterion = ['gini', 'entropy']
    iter_num = 0

    for c in criterion:
        iter_num += 1
        start = time.clock()
        cfr = DecisionTreeClassifier(criterion=c)
        cfr.fit(tran_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(test_y, p_out)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
    end = time.clock()
    print 'DecisionTree --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params


def NaiveBayes(tran_x, train_y, test_x, test_y):
    accuracy = 0
    iter_num = 0
    start = time.clock()
    cfr = GaussianNB()
    cfr.fit(tran_x, train_y)
    p_out = cfr.predict(test_x)
    accuracy_t = accuracy_score(test_y, p_out)
    if (accuracy < accuracy_t):
        accuracy = accuracy_t
        params = cfr.get_params()
    end = time.clock()
    print 'NaiveBayes --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params


def Bagging(tran_x, train_y, test_x, test_y):
    n_estimators_range = [x for x in range(10, 100)]
    accuracy = 0
    iter_num = 0
    start = time.clock()
    for n in n_estimators_range:
        iter_num += 1
        cfr = BaggingClassifier(LogisticRegression(), n_estimators=n,
                                max_samples=0.5, max_features=0.5)
        cfr.fit(tran_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(p_out, test_y)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
    end = time.clock()
    print 'svm --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params

def xgboost(tran_x, train_y, test_x, test_y):
    xgtrain = xgb.DMatrix(tran_x, label=train_y)

    xgtest = xgb.DMatrix(test_x,label=test_y)
    watchlist = [(xgtrain, 'train'),(xgtest, 'eval')]
    num_round = 1000
    min_child_weight = [x for x in range(1,11)]
    for n in min_child_weight:
        params = {
                'booster':'gbliner',
                'objective':'binary:logistic',
                'eta':0.1,
                'max_depth':2,
                'subsample':1.0,
                'min_child_weight':5,
                'colsample_bytree':0.2,
                'scale_pos_weight':0.1,
                'eval_metric':'auc',
                'gamma':0.2,
                'lambda':300
        }

        bst = xgb.train(params, xgtrain, num_round)
        #make prediction
        preds = bst.predict(xgtest)

        y_hat = preds
        y = xgtest.get_label()


        error_count = sum(y != (y_hat > 0.5))
        error_rate = float(error_count) / len(y_hat)
        print n
        print "样本总数：\t", len(y_hat)
        print "错误数目：\t%4d" % error_count
        print "错误率：\t%.2f%%" % (100 * error_rate)



def run_model(ensemble,trian_x,trian_y,test_x,test_y):
    # ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']

    for m in ensemble:
        if m=='SVM':
            SVM(trian_x,trian_y,test_x,test_y)
        if m=='RandomForest':
            RandomForest(trian_x,trian_y,test_x,test_y)
        if m == 'DecisionTree':
            DecisionTree(trian_x,trian_y,test_x,test_y)
        if m == 'xgboost':
            xgboost(trian_x,trian_y,test_x,test_y)
        if m == 'Linear':
            Linear(trian_x,trian_y,test_x,test_y)
        if m == 'NaiveBayes':
            NaiveBayes(trian_x,trian_y,test_x,test_y)
        if m == 'Bagging':
            Bagging(trian_x,trian_y,test_x,test_y)
