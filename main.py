#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""

from feature_engineering.features_model import *
from data_handle.table_from_mysql import CuData
from feature_preprocess.features_pre import fill_data

if __name__ == "__main__":

    # step1：读取 features_data,target_data,test_data
    cu = CuData(source="DB")

    model_start_date = ""
    model_end_date = ""

    # res = run_model('Linear', cu.data, model_start_date, model_end_date)

    current = CuData(source="DB", start_date='2017-10-11', end_date='2017-10-11')

    print current.data
    predict_data = fill_data(current.data)



    # model
    # ai_db_insert(res)


