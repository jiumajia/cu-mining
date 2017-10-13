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
from feature_preprocess import features_gear
from feature_preprocess.features_gear import F_STAG1
import numpy as np

if __name__ == "__main__":

    # step1：读取 features_data,target_data,test_data
    cu = CuData(source="DB")

    model_start_date = ""
    model_end_date = ""

    res = run_model('Linear', cu.data, model_start_date, model_end_date)

    current = CuData(source="DB", start_date='2017-06-30', end_date='2017-06-30')

    print current.data
    predict_data = fill_data(current.data)
    predict_data["target"] = '0'  # for process fake filling

    pd_data = features_gear.f_stage_one(predict_data)
    train_data = np.array(pd_data[F_STAG1[:-2]])

    print res.predict(train_data)
    # model
    # ai_db_insert(res)


