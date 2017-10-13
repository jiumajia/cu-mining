#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2016-09-13
预测模型构建
@author: zhoucuilian
"""

from mining.predict_models import run_model
from data_handle.table_from_mysql import CuData
import pandas as pd
import datetime
from sqlalchemy import create_engine
import requests,json


# 初始化数据库连接:
ALPHA_CONNECTION = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.140:20306/alpha')



def run():

    today = datetime.date.today()
    sql = 'select * from trade_calendar where today="%s"' % (today)
    trade_calendar = pd.read_sql(sql, ALPHA_CONNECTION, coerce_float=True)
    if trade_calendar['is_trading_day'][0] == 0:
        return
    else:
        pre_trade_day = trade_calendar['pre_trade_day']
        next_trade_day = trade_calendar['next_trade_day']
        print pre_trade_day
        pre_data = CuData(start_date=pre_trade_day, end_date=pre_trade_day,source="DB")
        print pre_data.data








    #
    # train_x = pd.read_csv('../datafiles/trian_x')
    # train_y = pd.read_csv()


if __name__ == "__main__":

    data_start_date = '2016-01-01'
    data_end_date = '2017-7-30'


    # step1：读取 features_data,target_data,test_data
    cu = CuData(start_date=data_start_date, end_date=data_end_date)
    prediction_data = CuData()
    #res = run_model('Linear', cu.data)
    run()
    url = 'http://172.16.88.163:9500/docs/#!/alert/alert_ai_prediction_create'
    #data = json.dump()
    #r = requests.post(url,data)


    # model
    #ai_db_insert(res)

#{'warm_start': False, 'C': 1.0, 'n_jobs': 1, 'verbose': 0, 'intercept_scaling': 1, 'fit_intercept': True, 'max_iter': 100, 'penalty': 'l2', 'multi_class': 'ovr', 'random_state': None, 'dual': False, 'tol': 0.0001, 'solver': 'liblinear', 'class_weight': None}
