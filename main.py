#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""

from mining.predict_models import run_model
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

    classf = run_model('Linear', cu.data, model_start_date, model_end_date)

    # predict
    current = CuData(source="DB", start_date='2017-10-13', end_date='2017-10-13', file='cu-630.csv')
    predict_data = fill_data(current.data)
    predict_data["target"] = '0'  # for process fake filling
    print predict_data
    pd_data = features_gear.f_stage_one(predict_data)
    train_data = np.array(pd_data[F_STAG1[:-2]])

    res = classf.predict(train_data)
    print res
    # model
    # ai_api_update(res)


#{'warm_start': False, 'C': 1.0, 'n_jobs': 1, 'verbose': 0, 'intercept_scaling': 1, 'fit_intercept': True, 'max_iter': 100, 'penalty': 'l2', 'multi_class': 'ovr', 'random_state': None, 'dual': False, 'tol': 0.0001, 'solver': 'liblinear', 'class_weight': None}
