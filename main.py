#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

from feature_engineering.features_model import *

if __name__ == "__main__":

    tstart = '2015-01-01'
    tend = '2017-6-20'

    # step1：读取 features_data,target_data,test_data
    data = get_pre_data(tstart, tend)

    # t1 = data.day > 5
    # t2 = data.day < 17
    # data = data[t1 & t2]

    #run_singlemodel(train_x,train_y,test_x,test_y)

    # (train_x,train_y,test_x,test_y)
    #ensemble = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']
    run_model(['SVM'], data)




