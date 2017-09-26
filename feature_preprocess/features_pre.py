#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-12
特征工程
@author: zhoucuilian
"""

import datetime

import pandas as pd
import talib
from dummy_features import Fdating
from data_handle.table_from_mysql import CuData



def get_quarter(date):
    """
        :return: QA = 1,2,3,or 4
    """
    if not isinstance(date, datetime.datetime):
       date = datetime.datetime.strptime(date, "%Y-%m-%d")
    query_month = int("%s" % (date.strftime("%m")))
    QA = query_month % 3 + 1
    return QA

def get_day(date):
    """
        :return: day = 1,2,3,....30
    """
    if not isinstance(date, datetime.datetime):
       date = datetime.datetime.strptime(date, "%Y-%m-%d")
    query_day = int("%s" % (date.strftime("%d")))

    return query_day




def fill_data(dataset,col_fill):
    """
    按列填充空缺值
    col_name
    method:fill method:median,bfill
    """
    for col_name in col_fill.keys():
        method =  col_fill[col_name]
        if method == 'median':
            dataset[col_name]= dataset[col_name].fillna(dataset[col_name].median()) #汇率用均值填充
        elif method == 'mean':
            dataset[col_name]= dataset[col_name].fillna(dataset[col_name].mean()) #汇率用中位数填充
        elif method == 'bfill':
            dataset[col_name] = dataset[col_name].fillna(method='bfill')  #库存用周五的数据填充
        elif method == 'pad':
            dataset[col_name] = dataset[col_name].fillna(method='pad')  #库存用周五的数据填充

    return dataset




def set_tagret(dataset,col_name,n):
    """
    col_name:列名
    n:天数
    """
    target_data = pd.DataFrame()
    dataset  = dataset.drop_duplicates().dropna(how='any')
    target_data["target"] = dataset[col_name].diff(-n)
    target_data.loc[target_data["target"]>=0,"target"] = 1
    target_data.loc[target_data["target"]<0,"target"] = 0

    dataset["target"] = target_data["target"]
    return dataset



def set_features(dataset):

    #feature
    p_data = pd.DataFrame()
    # D111: 期货结算价 ：  期货结算价(连续):阴极铜 - 期货结算价(连三):阴极铜
    p_data['d111'] = abs(dataset['S0068143'] - dataset['S0116880'])
    # D112: 长江有色升贴水 ： (铜升贴水:最小值:长江有色市场 + 铜升贴水:最大值:长江有色市场) /2
    p_data['d112'] = (dataset['S5806281'] + dataset['S5806282'])/2
    # # D121: LME铜升贴水(0-3)
    # p_data['d121'] = self.dataset['S5806058']
    # # D122: LME铜升贴水(3-15)
    # p_data['d122'] = self.dataset['S5808597']
    # D123: (最低溢价:上海电解铜:保税库(仓单) + 最高溢价:上海电解铜:保税库(仓单)) / 2
    #p_data['d123'] = (self.dataset['S5807322'] + self.dataset['S5807323'])/2
    # D211: LME仓单比例 ：  LME铜:注册仓单:合计:全球 / 总库存:LME铜
    p_data['d211'] = (dataset['S0164358'] / dataset['S0029752'])/2
    # D212 ： LME总库存： 总库存:LME铜
    #p_data['S0029752'] = self.dataset['S0029752']
    # D221: 国内仓单比例 ： 持仓仓单 / 库存小计:阴极铜:总计
    p_data['d221'] = (dataset['S0049493'] / dataset['S0049507'])/2
    # D222: 国内库存： 库存小计:阴极铜:总计
    p_data['d222'] = dataset['S0049507']
    # D511: LME铜持仓量 * 25（吨 / 手）
    p_data['d511'] = dataset['S5806052'] * 25
    # D512: 持仓比; LME铜持仓量 * 25（吨 / 手） / 总库存
    p_data['d512'] = (dataset['S5806052'] * 25 /dataset['S0029752']) / 2
    # D521: 国内持仓量 / 2 * 5(吨 / 手)
    p_data['d521'] = dataset['M0086399'] / 2 * 5
    # D522: 国内持仓比： 国内持仓量 / 2 * 5(吨 / 手) / 总库存
    p_data['d522'] = (dataset['M0086399'] / 2 * 5 / dataset['S0049507'])
    # D611: 升贴水差值： 铜升贴水:最大值:长江有色市场 - 铜升贴水:最小值:长江有色市场
    p_data['d611'] = dataset['S5806282'] - dataset['S5806281']
    # D612: 1 # 铜升贴水:最大值:上海金属 - 1#铜升贴水:最小值:上海金属
    p_data['d612'] = dataset['S0203260'] - dataset['S0203259']
#    p_data['d711'] = dataset['PE100058'] / dataset['MA000001']
#    p_data['d712'] = dataset['S0049493'] / dataset ['MA000001']
    #p_data['date'] = self.dataset['date']
    p_data['S0049493'] = dataset['S0049493']
    p_data['price_open'] = dataset['price_open']
    p_data['price_high'] = dataset['price_high']
    p_data['price_low'] = dataset['price_low']
    p_data['price_close'] = dataset['price_close']
    p_data['MA2'] = talib.MA(p_data['price_close'].values, timeperiod=2)  #调用talib计算5日均线的值
    p_data['MA3'] = talib.MA(p_data['price_close'].values, timeperiod=3)
    p_data['MA4'] = talib.MA(p_data['price_close'].values, timeperiod=4)
    p_data['MA5'] = talib.MA(p_data['price_close'].values, timeperiod=5)  #调用talib计算5日均线的值
    p_data['MA6'] = talib.MA(p_data['price_close'].values, timeperiod=6)
    p_data['MA10'] = talib.MA(p_data['price_close'].values, timeperiod=10)
    p_data['MA15'] = talib.MA(p_data['price_close'].values, timeperiod=15)
    #p_data['MA20'] = talib.MA(p_data['price_close'].values, timeperiod=20)
    #p_data['EMA20'] = talib.EMA(p_data['price_close'].values, timeperiod=20)
    p_data['QA'] = dataset['date'].map(get_quarter)
    p_data['day']  = dataset['date'].map(get_day)
    #index
    dataset = pd.merge(dataset,p_data,how = 'outer')
    dataset  = pd.concat([dataset],ignore_index=True)


    dic = {'S0049493':[2,3,4],'S0029752':[2,3,4]}
    dataset = Fdating(dataset, dic)
    dataset  = dataset.drop_duplicates().dropna(how='any')
    return dataset



def get_pre_data(tstart, tend):
    data = pd.DataFrame()
    try:
        cu = CuData(start_date='2012-01-01', end_date='2017-07-30')
        data = cu.data
    except Exception,e:
        print e.message
        try:
            pass
        except Exception,e:
            print e.message
            return data


    #col_fill = {'USE00020':'median','S0049507':'pad','PE100058':'pad','MA000001':'pad'}
    col_fill = {'USE00020':'median','S0049507':'pad','PE100058':'pad','PE100042':'bfill'}

    data = fill_data(data,col_fill)
    #data.to_csv("/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/cu_fill.csv")
    data = fill_data(data, col_fill)
    data = set_tagret(data, 'S0181392', 1)
    # data_handle.to_csv("/Users/zhoucuilian/PycharmProjects/cu_mining/datafiles/cu_fill.csv")   already have in front function
    data = set_features(data)
    b1 = data.date >= tstart
    b2 = data.date <= tend
    data = data[b1 & b2]
    data = set_features(data)
    return data









