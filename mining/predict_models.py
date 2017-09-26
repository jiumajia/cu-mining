#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""
from mining import model_Bagging, model_DecisionTree, model_LR, model_NaiveBayes, model_RF, model_SVM, model_XGB
from sklearn import preprocessing
import numpy as np
from data_handle.table_info import features_list
from sklearn.cross_validation import *

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


def run_model(ensemble, data):
    # ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']
    train_data = np.array(data[features_list])
    target_data = np.array(data['target'])

    preprocessing.scale(train_data)

    train_x, test_x, train_y, test_y = train_test_split(train_data, target_data, test_size=0.2,random_state=42)

    print '训练集样本数:',len(train_x), '  测试集样本数:',len(test_x)

    for m in ensemble:
        if m == 'SVM':
            model_SVM.SVM(train_x, train_y, test_x, test_y)
        if m =='RandomForest':
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
