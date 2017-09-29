#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""
from mining import model_Bagging, model_DecisionTree, model_LR, model_NaiveBayes, model_RF, \
    model_SVM, model_XGB, model_GBT
from sklearn.model_selection import train_test_split
from feature_preprocess.features_pre import get_pre_data

def run_model(ensemble, data):
    # ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']

    train_data, target_data = get_pre_data(data)

    train_x, test_x, train_y, test_y = train_test_split(train_data, target_data, test_size=0.2, random_state=42)

    print '训练集样本数:',len(train_x), '  测试集样本数:',len(test_x)

    # for m in ensemble:
    m = ensemble
    if m == 'SVM':
        model_SVM.SVM(train_x, train_y, test_x, test_y)
    if m == 'RandomForest':
        model_RF.RandomForest(train_x, train_y, test_x, test_y)
    if m == 'DecisionTree':
        model_DecisionTree.DecisionTree(train_x, train_y, test_x, test_y)
    if m == 'xgboost':
        model_XGB.xgb(train_x, train_y, test_x, test_y)
    if m == 'Linear':
        model_LR.Linear(train_x, train_y, test_x, test_y)
    if m == 'NaiveBayes':
        model_NaiveBayes.NaiveBayes(train_x, train_y, test_x, test_y)
    if m == 'Bagging':
        model_Bagging.Bagging(train_x, train_y, test_x, test_y)
    if m == 'GBT':
        model_GBT.GBT(train_x, train_y, test_x, test_y)
