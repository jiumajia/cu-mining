#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""
from mining import model_Bagging, model_DecisionTree, model_LR, model_NaiveBayes, model_RF, model_SVM, model_XGB
from sklearn import preprocessing

def Standardized_data(train):
    """
    标准化训练集、测试集
    """
    scaler = preprocessing.StandardScaler().fit(train)
    train_data = scaler.transform(train)
    #test_data = scaler.transform(test)

    #return train_data,test_data
    return train_data

def Normalization_data(train,test):
    """
    正则化训练集、测试集
    """
    normalizer = preprocessing.Normalizer().fit(train)
    train_data = normalizer.transform(train)
   # test_data = normalizer.transform(test)

    #return train_data,test_data
    return train_data


def run_model(ensemble,trian_x,trian_y,test_x,test_y):
    # ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']

    # for m in ensemble:
    m = ensemble
    if m=='SVM':
        model_SVM.SVM(trian_x, trian_y, test_x, test_y)
    if m=='RandomForest':
        model_RF.RandomForest(trian_x, trian_y, test_x, test_y)
    if m == 'DecisionTree':
        model_DecisionTree.DecisionTree(trian_x, trian_y, test_x, test_y)
    if m == 'xgboost':
        model_XGB.xgb(trian_x, trian_y, test_x, test_y)
    if m == 'Linear':
        model_LR.Linear(trian_x, trian_y, test_x, test_y)
    if m == 'NaiveBayes':
        model_NaiveBayes.NaiveBayes(trian_x, trian_y, test_x, test_y)
    if m == 'Bagging':
        model_Bagging.Bagging(trian_x, trian_y, test_x, test_y)
