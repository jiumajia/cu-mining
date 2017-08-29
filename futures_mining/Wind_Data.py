#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

import pandas as pd
import datetime
import talib
from info.db_info import alpha_con
import config
from info.table_info import *
from futuresdating import Fdating


def get_quarter(date):
    """
        :return: start_day,end_day
    """
    if not isinstance(date, datetime.datetime):
       date = datetime.datetime.strptime(date, "%Y-%m-%d")
    query_month = int("%s" % (date.strftime("%m")))
    QA = query_month % 3 + 1
    return QA



class Wind_Data(object):

    def __init__(self,table_name,col_name):
        self.table_name = table_name
        self.col_name = col_name
        self.dataset = pd.DataFrame(columns=["date"])

    def read_data(self,tstart,tend):
        #从table:data_wind,future_exchange 读取数据
        for tn in self.table_name:
            for cn in self.col_name[tn]:
                sql = config.getConfig(tn,cn) % (tstart,tend)
                data_slice = pd.read_sql(sql,alpha_con,coerce_float=True)
                data_slice['date'] = pd.to_datetime(data_slice['date'],format='%Y-%m-%d')
                #连接data_slice
                self.dataset = pd.merge(self.dataset,data_slice,how = 'outer')

        self.dataset = self.dataset.sort_values(by="date")
        self.dataset.to_csv('../datasets/cu.csv')
        return self.dataset


    def fill_data(self,col_name,method):
        """
        按列填充空缺值
        col_name
        method:fill method(mean,bfill)
        """

        if method == 'mean':
            self.dataset[col_name]= self.dataset[col_name].fillna(self.dataset[col_name].mean()) #汇率用均值填充
        elif method == 'bfill':
            self.dataset[col_name] = self.dataset[col_name].fillna(method='bfill')  #库存用周五的数据填充


    def set_tagret(self,col_name,n):
        #target

        target_data = pd.DataFrame()
        self.dataset  = self.dataset.drop_duplicates().dropna(how='any')
        target_data["target"] = self.dataset[col_name].diff(-n)
        target_data.loc[target_data["target"]>=0,"target"] = 0
        target_data.loc[target_data["target"]<0,"target"] = -1
        # target_data.dropna(inplace=True)
        self.dataset["target"] = target_data["target"]
        self.dataset.to_csv('../datasets/cu.csv')



    def get_target(self):

        return self.dataset['target']

    def set_features(self):
        #feature
        p_data = pd.DataFrame()
        # D111: 期货结算价 ：  期货结算价(连续):阴极铜 - 期货结算价(连三):阴极铜
        p_data['d111'] = abs(self.dataset['S0068143'] - self.dataset['S0116880'])
        # D112: 长江有色升贴水 ： (铜升贴水:最小值:长江有色市场 + 铜升贴水:最大值:长江有色市场) /2
        p_data['d112'] = (self.dataset['S5806281'] + self.dataset['S5806282'])/2
        # D121: LME铜升贴水(0-3)
        p_data['d121'] = self.dataset['S5806058']
        # D122: LME铜升贴水(3-15)
        p_data['d122'] = self.dataset['S5808597']
        # D123: (最低溢价:上海电解铜:保税库(仓单) + 最高溢价:上海电解铜:保税库(仓单)) / 2
        #p_data['d123'] = (self.dataset['S5807322'] + self.dataset['S5807323'])/2
        # D211: LME仓单比例 ：  LME铜:注册仓单:合计:全球 / 总库存:LME铜
        p_data['d211'] = (self.dataset['S0164358'] / self.dataset['S0029752'])/2
        # D212 ： LME总库存： 总库存:LME铜
        p_data['S0029752'] = self.dataset['S0029752']
        # D221: 国内仓单比例 ： 持仓仓单 / 库存小计:阴极铜:总计
        p_data['d221'] = (self.dataset['S0049493'] / self.dataset['S0049507'])/2
        # D222: 国内库存： 库存小计:阴极铜:总计
        p_data['d222'] = self.dataset['S0049507']
        # D511: LME铜持仓量 * 25（吨 / 手）
        p_data['d511'] = self.dataset['S5806052'] * 25
        # D512: 持仓比; LME铜持仓量 * 25（吨 / 手） / 总库存
        p_data['d512'] = (self.dataset['S5806052'] * 25 / self.dataset['S0029752']) / 2
        # D521: 国内持仓量 / 2 * 5(吨 / 手)
        p_data['D521'] = self.dataset['M0086399'] / 2 * 5
        # D522: 国内持仓比： 国内持仓量 / 2 * 5(吨 / 手) / 总库存
        p_data['D522'] = (self.dataset['M0086399'] / 2 * 5 / self.dataset['S0049507'])
        # D611: 升贴水差值： 铜升贴水:最大值:长江有色市场 - 铜升贴水:最小值:长江有色市场
        p_data['d611'] = self.dataset['S5806282'] - self.dataset['S5806281']
        # D612: 1 # 铜升贴水:最大值:上海金属 - 1#铜升贴水:最小值:上海金属
        p_data['d612'] = self.dataset['S0203260'] - self.dataset['S0203259']
        p_data['d711'] = self.dataset['USE00020']
        #p_data['date'] = self.dataset['date']
        p_data['S0049493'] = self.dataset['S0049493']
        p_data['price_open'] = self.dataset['price_open']
        p_data['price_high'] = self.dataset['price_high']
        p_data['price_low'] = self.dataset['price_low']
        p_data['price_close'] = self.dataset['price_close']
        p_data['MA5'] = talib.MA(p_data['price_close'].values, timeperiod=5)  #调用talib计算5日均线的值
        p_data['MA10'] = talib.MA(p_data['price_close'].values, timeperiod=10)
        p_data['MA15'] = talib.MA(p_data['price_close'].values, timeperiod=15)
        p_data['MA20'] = talib.MA(p_data['price_close'].values, timeperiod=20)
        p_data['EMA20'] = talib.EMA(p_data['price_close'].values, timeperiod=20)
        p_data['QA'] = self.dataset['date'].map(get_quarter)

        self.dataset = pd.merge(self.dataset,p_data,how = 'outer')

        self.dataset  = pd.concat([self.dataset],ignore_index=True)

        dic = {'S0049493':[2,3,4],'S0029752':[2,3,4]}
        self.dataset = Fdating(self.dataset,dic)



    def get_fdata(self):

        featuredata = pd.DataFrame()
        targetdata = pd.DataFrame()
        self.dataset = self.dataset.dropna(how='any')
        for name in self.dataset.columns:
            if name in features_list:
                featuredata[name] = self.dataset[name]
        targetdata['target'] = self.dataset['target']

        return featuredata,targetdata


    def get_valuesbycol(self,col_name):

        return self.dataset[col_name].values

    def __getattr__(self, item):

        return self.item



if __name__ == "__main__":


    wind_data = Wind_Data(table_name,table_col)
    #step1:读取数据
    wind_data.read_data('2015-1-1','2017-6-28')
    #step2:填充数据:USE00020,S0049507
    wind_data.fill_data('USE00020','mean')
    wind_data.fill_data('S0049507','bfill')
    wind_data.set_tagret('S0181392',1)
    wind_data.set_features()

















