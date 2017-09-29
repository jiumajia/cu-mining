#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import xgboost as xgb
# from xgboost.sklearn import XGBClassifier
#
# def xgboost(tran_x, train_y, test_x, test_y):
#     xgtrain = xgb.DMatrix(tran_x, label=train_y)
#     xgtest = xgb.DMatrix(test_x,label=test_y)
#     watchlist = [(xgtrain, 'train'),(xgtest, 'eval')]
#     num_round = 1000
#     min_child_weight = [x for x in range(1,11)]
#     for n in min_child_weight:
#         params = {
#                 'booster':'gbliner',
#                 'objective':'binary:logistic',
#                 'eta':0.1,
#                 'max_depth':2,
#                 'subsample':1.0,
#                 'min_child_weight':5,
#                 'colsample_bytree':0.2,
#                 'scale_pos_weight':0.1,
#                 'eval_metric':'auc',
#                 'gamma':0.2,
#                 'lambda':300
#         }
#
#         bst = xgb.train(params, xgtrain, num_round)
#         #make prediction
#         preds = bst.predict(xgtest)
#
#         y_hat = preds
#         y = xgtest.get_label()
#
#
#         error_count = sum(y != (y_hat > 0.5))
#         error_rate = float(error_count) / len(y_hat)
#         print n
#         print "样本总数：\t", len(y_hat)
#         print "错误数目：\t%4d" % error_count
#         print "错误率：\t%.2f%%" % (100 * error_rate)
