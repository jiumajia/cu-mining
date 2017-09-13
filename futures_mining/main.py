#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""


import numpy as np
from correction import get_statics
from info.table_info import features_list
from sklearn import preprocessing
from data_select import *
from predict_models import SVM, RandomForest, DecisionTree,Linear,NaiveBayes,Bagging
from features_models import feature_RFE
from sklearn import cross_validation

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


def model(ensemble,trian_x,trian_y,test_x,test_y):
    # model = ['SVM','RandomForest','Linear','DecisionTree','NaiveBayes','Bagging']

    for m in ensemble:
        if m=='SVM':
            SVM(trian_x,trian_y,test_x,test_y)
        if m=='RandomForest':
            RandomForest(trian_x,trian_y,test_x,test_y)
        if m == 'DecisionTree':
            DecisionTree(trian_x,trian_y,test_x,test_y)
        if m == 'DecisionTree':
            DecisionTree(trian_x,trian_y,test_x,test_y)
        if m == 'Linear':
            Linear(trian_x,trian_y,test_x,test_y)
        if m == 'NaiveBayes':
            NaiveBayes(trian_x,trian_y,test_x,test_y)
        if m == 'Bagging':
            Bagging(trian_x,trian_y,test_x,test_y)


def merge_model(trian_x,trian_y,test_x,test_y):
    pass

def run_singlemodel(trian_x,trian_y,test_x,test_y):

    rank = feature_RFE(trian_x,trian_y)
    for i in range(0,len(rank)):
        index = [x for x in range(0,len(rank[i])) if rank[i][x]==1]
        print [features_list[x] for x in index]
        trian = trian_x[:,index]
        test = test_x[:,index]
        #step3 ：minning
        model(['Linear'],trian,trian_y,test,test_y)


def run_mergemodel(trian_x,trian_y,test_x,test_y):
    pass





if __name__ == "__main__":
    tstart = '2013-01-01'
    tend = '2017-6-20'

    # step1：读取 features_data,target_data,test_data
    data = get_learningdata(tstart,tend)
    data = data[data.QA == 2]
    t1 = data.day > 5
    t2 = data.day < 17
    data = data[t1 & t2]
    train_data = np.array(data[features_list])
    print features_list
    target_data = np.array(data['target'])

    preprocessing.scale(train_data)

    trian_x,test_x,trian_y,test_y= cross_validation.train_test_split(train_data,target_data, test_size=0.3, random_state=42)



    print '训练集样本数:',len(trian_x)
    print '测试集样本数:',len(test_x)

    run_singlemodel(trian_x,trian_y,test_x,test_y)


    # index = [0,1,4,5,6,7,8,9,10,11,12,18,19,20,22,23,24,25,30,31,32,33,34,35]
    # trian = trian_x[:,index]
    # test = test_x[:,index]
    #
    #
    # p_out = Linear(trian,trian_y,test,test_y)
    # p_index0 = [x for x in range(0,len(p_out)) if p_out[x]==0]
    # p_index1 = [x for x in range(0,len(p_out)) if p_out[x]==-1]
    # # p_out = np.array([p_out])
    # #test = np.concatenate((test,p_out.T),axis=1)
    #
    # # print test
    # # temp = int(len(test) * 7/ 10 )
    # # model(['RandomForest'],test[:temp],test_y[:temp],test[temp:],test_y[temp:])
    # # #
    # test1 = test[p_index0]
    # test2 = test[p_index1]
    # test
    # temp = int(len(test1) * 7/ 10 )
    # model(['RandomForest'],test1[:temp],test_y[:temp],test[temp:],test_y[temp:]),



