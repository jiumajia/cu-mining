#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""

from feature_engineering.features_model import *
from data_handle.table_from_mysql import CuData

if __name__ == "__main__":

    data_start_date = '2015-01-01'
    data_end_date = '2017-7-30'

    # step1：读取 features_data,target_data,test_data
    cu = CuData(start_date=data_start_date, end_date=data_end_date)
    run_model('Linear', cu.data)



