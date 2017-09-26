#!/usr/bin/env python
# -*- coding: utf-8 -*-

from feature_engineering.features_model import *
from data_handle.table_from_mysql import CuData

if __name__ == "__main__":

    data_start_date = '2015-01-01'
    data_end_date = '2017-6-20'

    # step1：读取 features_data,target_data,test_data
    cu = CuData(start_date=data_start_date, end_date=data_end_date)

    run_model(['SVM'], cu.data)




