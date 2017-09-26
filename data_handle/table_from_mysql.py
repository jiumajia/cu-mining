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
ALPHA_CONNECTION = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.140:20306/alpha')

#alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.163:20306/alpha')


class CuData(object):
    _file_path = "../datafiles/cu.csv"

    def __init__(self):
        self.table_col_map = table_col_map
        self.dataset = pd.DataFrame(columns=["date"])

    def __init__(self, start_date='2011-01-01', end_date='2017-07-30', source="DB"):
        self.table_col_map = table_col_map
        self.dataset = pd.DataFrame(columns=["date"])
        self.get_data(start_date, end_date, source)

    def get_data(self, start_date='2011-01-01', end_date='2017-07-30', source="DB"):
        if source == "DB":
            read_data = self._get_data_from_mysql(start_date, end_date)
        elif source == "FILE":
            read_data = pd.read_csv(self._file_path)
        else:
            raise ValueError("You must provide source : DB or FILE")

        return read_data

    def _data_to_csv(self, path=_file_path):
        try:
            self.dataset.to_csv(path)
        except Exception, e:
            raise e

    def _get_data_from_mysql(self, start_date='2011-01-01', end_date='2017-07-30'):
        # 从mysql数据库 读取数据
        for tn in self.table_col_map.keys():
            for cn in self.table_col_map[tn]:
                sql = config.getConfig(tn, cn) % (start_date, end_date)
                data_slice = pd.read_sql(sql, ALPHA_CONNECTION, coerce_float=True)
                data_slice['date'] = pd.to_datetime(data_slice['date'], format='%Y-%m-%d')
                # 连接data_slice
                self.dataset = pd.merge(self.dataset, data_slice, how='outer')

        self.dataset = self.dataset.sort_values(by="date")

        self._data_to_csv()

        return self.dataset

    @property
    def data(self):
        """  property of CuData """
        return self.dataset


if __name__ == "__main__":
    cu = CuData(start_date='2012-01-01', end_date='2017-07-30')
    print cu.data






















