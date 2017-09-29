#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import config
from data_handle.table_info import table_col_map
from sqlalchemy import create_engine


# 初始化数据库连接:
ALPHA_CONNECTION = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.140:20306/alpha')

#alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.163:20306/alpha')


class CuData(object):

    """
     CuData return 2011 -2017 cu data
    """

    def __init__(self, **kwargs):
        self.table_col_map = table_col_map
        self.dataset = pd.DataFrame(columns=["date"])
        datafile_path = os.path.dirname(os.path.abspath(os.path.abspath(os.path.dirname(__file__))))
        self._file_path = datafile_path + "/datafiles/cu.csv"
        self.get_data(**kwargs)

    def get_data(self, start_date='2011-01-01', end_date='2017-07-30', source="DB"):
        self.start_date = start_date
        self.end_date = end_date
        if source == "DB":
            self.dataset = self._get_data_from_mysql(start_date, end_date)
        elif source == "FILE":
            self.dataset = pd.read_csv(self._file_path)  # waiting for function "_get_data_from_file"
        else:
            raise ValueError("You must provide source : DB or FILE")

        return self.dataset

    def _data_to_csv(self, path=None):
        if not path:
            path = self._file_path
        try:
            self.dataset.to_csv(path)
        except Exception, e:
            raise e

    def _get_data_from_file(self, path=None):
        if not path:
            path = self._file_path
        pass

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
    print cu.start_date
    print cu.end_date
    # print cu.data






















