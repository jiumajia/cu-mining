#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

import numpy as np
from sklearn.cross_validation import *
from sklearn import preprocessing
from feature_preprocess.features_pre import get_pre_data
from matplotlib import pyplot as plt
from feature_engineering.features_model import *
from data.table_info import features_list


if __name__ == "__main__":

    tstart = '2015-01-01'
    tend = '2017-6-20'

    # step1：读取 features_data,target_data,test_data
    data = get_pre_data(tstart,tend)

    # t1 = data.day > 5
    # t2 = data.day < 17
    # data = data[t1 & t2]
    train_data = np.array(data[features_list])
    target_data = np.array(data['target'])

    preprocessing.scale(train_data)

    train_x,test_x,train_y,test_y = train_test_split(train_data,target_data, test_size=0.2,random_state=42)

    print '训练集样本数:',len(train_x)
    print '测试集样本数:',len(test_x)

    #run_singlemodel(train_x,train_y,test_x,test_y)

    (train_x,train_y,test_x,test_y)
    #ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']
    run_model(['xgboost'],train_x,train_y,test_x,test_y)




