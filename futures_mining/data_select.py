#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

import calendar
import datetime

import pandas as pd

from Wind_Data import Wind_Data
from info.table_info import table_name,table_col

def get_period(year, prediction_day):
    """
        :return: start_day,end_day
    """
    prediction_day = datetime.datetime.strptime(prediction_day, "%Y-%m-%d")
    query_month = int("%s" % (prediction_day.strftime("%m")))
    quarter = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    for item in quarter:
        if query_month in item:
            start_day = "%s-%s-%s" % (year, item[0], '1')
            end_day = "%s-%s-%s" % (year, item[-1], calendar.monthrange(year, item[-1])[1])
            return start_day, end_day


def select_data(dataset,tstart=None,tend=None):
    t_data = pd.DataFrame()
    tstart = pd.datetime.strptime(tstart,'%Y-%m-%d')
    tend = pd.datetime.strptime(tend,'%Y-%m-%d')
    strtotime=lambda x:pd.datetime.strptime(str(x),'%Y-%m-%d')
    dataset['date'] = dataset['date'].map(strtotime)
    b1 = dataset.date>=tstart
    b2 = dataset.date<=tend
    dataset = dataset[b1 & b2]
    return dataset

def get_quarterdata(query_day):
    year = [2015,2016,2017]
    target_data = pd.DataFrame()
    features_data = pd.DataFrame()

    year = [2015,2016,2017]
    target_data = pd.DataFrame()
    features_data = pd.DataFrame()
    for y in year:
        tstart,tend = get_period(y,query_day)

        wind_data = Wind_Data(table_name,table_col)
        #step1:读取数据
        wind_data.read_data(tstart,tend)
        #step2:填充数据:USE00020汇率,S0049507库存
        wind_data.fill_data('USE00020','mean')
        wind_data.fill_data('S0049507','bfill')
        #step3:set target 结算价
        target = wind_data.get_tagret('S0181392')
        #step4:get_features
        features = wind_data.get_features()[:-1]
        target_data = pd.concat([target_data,target])
        features_data = pd.concat([features_data,features])

    return features_data,target_data

def get_learningdata():

    tstart = '2015-1-1'
    tend = '2017-8-25'

    wind_data = Wind_Data(table_name,table_col)
    #step1:读取数据
    wind_data.read_data(tstart,tend)
    #step2:填充数据:USE00020,S0049507
    wind_data.fill_data('USE00020','mean')
    wind_data.fill_data('S0049507','bfill')
    wind_data.set_tagret('S0181392',1)
    wind_data.set_features()
    featuredata,targetdata = wind_data.get_fdata()
    return featuredata,targetdata



def get_test(query_day):

    wind_data = Wind_Data(table_name,table_col)
    #step1:读取数据
    wind_data.read_data(query_day,query_day)
    #step4:get_features
#    features_data = wind_data.get_features()
    features_data = pd.DataFrame()
    return features_data


if __name__ == '__main__':
    prediction_day = '2017-6-22'
    # start_day, end_day = get_period(2017,prediction_day)
    get_learningdata(prediction_day)
    get_test(prediction_day)





