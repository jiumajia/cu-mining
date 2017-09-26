#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""
import numpy as np
import pandas as pd
from sklearn.cross_validation import *
from sklearn import preprocessing
from feature_engineering.features_model import *
from data.table_info import features_list
from mining.Xgboost import run_xgboost
from feature_preprocess.features_pre import get_pre_data


if __name__ == "__main__":

    tstart = '2012-01-01'
    tend = '2017-7-1'

    # step1：读取 features_data,target_data,test_data
    data = get_pre_data(tstart,tend)

    train_data = np.array(data[features_list])
    data[features_list].to_csv('/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/cu.csv')
    target_data = np.array(data['target'])
    #
    # data = data[features_list].diff(1)
    # data[data[:]>=0] = 1
    # data[data[:]<0] = 0
    # train_data = np.array(data[1:])
    preprocessing.scale(train_data)
    print train_data



    print train_data.shape,target_data.shape

    train_x,test_x,train_y,test_y = train_test_split(train_data,target_data, test_size=0.2,random_state=42)
    pd.DataFrame(train_x).to_csv('/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/train_x.csv')
    pd.DataFrame(train_y).to_csv('/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/train_y.csv')
    pd.DataFrame(test_x).to_csv('/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/test_x.csv')
    pd.DataFrame(test_y).to_csv('/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/test_y.csv')


    print '训练集样本数:',len(train_x)
    print '测试集样本数:',len(test_x)

    #run_singlemodel(train_x,train_y,test_x,test_y)

    #ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']
    #run_model(['xgboost'],train_x,train_y,test_x,test_y)
    run_xgboost(train_x,train_y,test_x,test_y)




