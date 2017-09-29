#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-12
特征工程
@author: zhoucuilian
"""

import pandas as pd
from feature_preprocess import features_gear
import numpy as np
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

def fill_data(dataset, col_fill):
    """
    按列填充空缺值
    col_name
    method:fill method:median,bfill
    """
    for col_name in col_fill.keys():
        method = col_fill[col_name]
        if method == 'median':
            dataset[col_name] = dataset[col_name].fillna(dataset[col_name].median())  # 汇率用均值填充
        elif method == 'mean':
            dataset[col_name] = dataset[col_name].fillna(dataset[col_name].mean())  # 汇率用中位数填充
        elif method == 'bfill':
            dataset[col_name] = dataset[col_name].fillna(method='bfill')  # 库存用周五的数据填充
        elif method == 'pad':
            dataset[col_name] = dataset[col_name].fillna(method='pad')  # 库存用周五的数据填充

    return dataset

def set_tagret(dataset, col_name, n):
    """
    col_name:列名
    n:天数
    """
    # target_data = pd.DataFrame()
    dataset = dataset.dropna(subset=['S0181392'])
    # dataset = dataset.drop_duplicates().dropna(how='any')
    # target_data["target"] = dataset[col_name].diff(-n)
    # dataset.loc[dataset["target"] >= 0, "target"] = 1
    # dataset.loc[dataset["target"] < 0, "target"] = 0

    target_data = np.where(dataset['S0181392'].diff(-n) >= 0, 0, 1)
    dataset["target"] = target_data
    dataset.to_csv('.csv')
    return dataset

def get_pre_data(data):

    # step1 filling empty , missing data
    col_fill = {'USE00020': 'median', 'S0049507': 'pad', 'PE100058': 'pad', 'MA000001': 'pad','PE100042':'bfill'}
    data = fill_data(data, col_fill)

    # step2 set target
    data = set_tagret(data, 'S0181392', 1)

    # step3 set features
    train_data, target_data = features_gear.set_features(data, stage="f_stage_two")

    return train_data, target_data
