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

    # step1：读取 features_data,target_data,test_data
    cu = CuData(source="DB")

    model_start_date = '2011-01-01'
    model_end_date = '2017-07-30'

    res = run_model('GBT', cu.data, model_start_date, model_end_date)

    # model
    # ai_db_insert(res)


