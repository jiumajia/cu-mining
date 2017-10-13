#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-12
特征工程
@author: zhoucuilian
"""

from feature_preprocess import features_gear
import numpy as np
import pandas as pd
from sklearn import preprocessing

def Standardized_data(train,test):
    """
    标准化训练集、测试集
    """
    scaler = preprocessing.StandardScaler().fit(train)
    train_data = scaler.transform(train)
    test_data = scaler.transform(test)

    #return train_data,test_data
    return train_data

def fill_data(dataset):
    """
    按列填充空缺值
    col_name
    method:fill method:median,bfill
    """
    col_fill = {'USE00020': 'median', 'S0049507': 'pad', 'PE100058': 'pad', 'MA000001': 'pad', 'PE100042': 'bfill'}

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
    #S0181392 去除空值
    dataset = dataset.dropna(subset=['S0181392'])
    target_data = np.where(dataset['S0181392'].diff(-n) >= 0, 0, 1)
    dataset["target"] = target_data
    # dataset.to_csv('.csv')

    return dataset

def get_pre_data(data, start_date, end_date):

    # step1 filling empty , missing data
    col_fill = {'USE00020': 'median', 'S0049507': 'pad', 'PE100058': 'pad', 'MA000001': 'pad','PE100042':'bfill','price_close':'pad'}
    data = fill_data(data)

    # step2 set target
    data = set_tagret(data, 'S0181392', 1)

    # step3 set features
    train_data, target_data = features_gear.set_features(data, stage="f_stage_one")
    pd.DataFrame(train_data).to_csv('train.csv')
    # step3 set features   # pending better to be merged with train and target !!!
    train_data, target_data = features_gear.set_features(data, start_date, end_date, stage="f_stage_one")

    return train_data, target_data
