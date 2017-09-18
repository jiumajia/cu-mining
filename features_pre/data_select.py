#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

import pandas as pd



#
# def get_period(year, prediction_day):
#     """
#         :return: start_day,end_day
#     """
#     prediction_day = datetime.datetime.strptime(prediction_day, "%Y-%m-%d")
#     query_month = int("%s" % (prediction_day.strftime("%m")))
#     quarter = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#     for item in quarter:
#         if query_month in item:
#             start_day = "%s-%s-%s" % (year, item[0], '1')
#             end_day = "%s-%s-%s" % (year, item[-1], calendar.monthrange(year, item[-1])[1])
#             return start_day, end_day

#
# def select_data(dataset,tstart=None,tend=None):
#     tstart = pd.datetime.strptime(tstart,'%Y-%m-%d')
#     tend = pd.datetime.strptime(tend,'%Y-%m-%d')
#     strtotime=lambda x:pd.datetime.strptime(str(x),'%Y-%m-%d')
#     dataset['date'] = dataset['date'].map(strtotime)
#     b1 = dataset.date>=tstart
#     b2 = dataset.date<=tend
#     dataset = dataset[b1 & b2]
#     return dataset
#
# #
# # def get_quarterdata(query_day):
# #     year = [2015,2016,2017]
# #     target_data = pd.DataFrame()
# #     features_data = pd.DataFrame()
# #
# #     year = [2015,2016,2017]
# #     target_data = pd.DataFrame()
# #     features_data = pd.DataFrame()
# #     for y in year:
# #         tstart,tend = get_period(y,query_day)
# #
# #         wind_data = Wind_Data(table_name,table_col)
# #         #step1:读取数据
# #         wind_data.read_data(tstart,tend)
# #         #step2:填充数据:USE00020汇率,S0049507库存
# #         wind_data.fill_data('USE00020','mean')
# #         wind_data.fill_data('S0049507','bfill')
# #         #step3:set target 结算价
# #         target = wind_data.get_tagret('S0181392')
# #         #step4:get_features
# #         features = wind_data.get_features()[:-1]
# #         target_data = pd.concat([target_data,target])
# #         features_data = pd.concat([features_data,features])
# #
# #     return features_data,target_data




def read_from_mysql():
    wind_data = Wind_Data(table_name,table_col)
    #step1:读取数据
    wind_data.read_data()
    #step2:填充数据:USE00020,S0049507,PE100058,MA000001
    wind_data.fill_data('USE00020','median')
    wind_data.fill_data('S0049507','pad')
    wind_data.fill_data('PE100058','pad')
    wind_data.fill_data('MA000001','pad')
    wind_data.set_tagret('S0181392',1)
    wind_data.set_features()
    mysql_data = wind_data.dataset
    mysql_data.to_csv("../datasets/mysql_data.csv")
    return mysql_data

def read_from_wind():
    pass



def get_learningdata(tstart,tend):

    data = read_from_mysql()
    print data['date']
    b1 = data.date>=tstart
    b2 = data.date<=tend
    data = data[b1 & b2]
    return data













