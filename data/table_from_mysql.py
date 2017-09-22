#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

import pandas as pd

import config

from table_info import table_col_map
from sqlalchemy import create_engine


# 初始化数据库连接:
alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.140:20306/alpha')

#alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.163:20306/alpha')


class Cu_Data(object):

    def __init__(self,table_col_map):
        self.table_col_map = table_col_map
        self.dataset = pd.DataFrame(columns=["date"])

    def get_data(self,tstart = '2011-01-01',tend = '2017-07-30'):
        #从mysql数据库 读取数据
        for tn in self.table_col_map.keys():
            for cn in self.table_col_map[tn]:
                sql = config.getConfig(tn,cn) % (tstart,tend)
                data_slice = pd.read_sql(sql,alpha_con,coerce_float=True)
                data_slice['date'] = pd.to_datetime(data_slice['date'],format='%Y-%m-%d')
                #连接data_slice
                self.dataset = pd.merge(self.dataset,data_slice,how = 'outer')

        self.dataset = self.dataset.sort_values(by="date")
        self.dataset.to_csv("/Users/zhoucuilian/PycharmProjects/cu_mining/datasets/cu.csv")
        return self.dataset

def get_data_from_mysql(tstart,tend):
    cu = Cu_Data(table_col_map)
    return cu.get_data(tstart,tend)


if __name__ == "__main__":
    get_data_from_mysql(tstart = '2011-01-01',tend = '2017-07-30')
























