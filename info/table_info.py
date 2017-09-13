#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

table_name = {'data_wind', 'future_exchange', 'data_sina_day_kline','future_bwd_summary','data_artificial'}

symbol = ["S5806281", "S5806282", "S5807322", "S5807323", "S5806058",
          "S5808597", "S0116880", "S0068143", "S0029752", "S0164358",
          "S5806052", "S0049507", "S0049493", "S0181392", "S0203259",
          "S0203260", "M0086399", "USE00020"]

table_col = {
            'data_wind': [
                "S5806281",
                "S5806282",
                "S5807322",
                "S5807323",
                "S5806058",
                "S5808597",
                "S0116880",
                "S0068143",
                "S0029751",
                "S0029752",
                "S0164358",
                "S5806052",
                "S0049507",
                "S0049493",
                "S0181392",
                "S0203259",
                "S0203260",
                "M0086399"
            ],
             'spot_warehouse_receipt': [
                 "USE00105"  # 期货:仓单:铜:LME#
             ],
             'data_enanchu': [
                 "ENANCHU_800",  # 上海铜现货升贴水高价
                 "ENANCHU_801"  # 上海铜现货升贴水低价
             ],
             'day_preprocess': [
                 "PE201011",  # 铜连一合约结算价
                 "PE201004"  # 主连持仓量
             ],
             'future_exchange': [
                 "USE00020"  # 外汇:1周汇率:报价:USD
             ],
             'data_sina_day_kline': [
                 "price_open",
                 "price_high",
                 "price_low",
                 "price_close"
             ],
               'data_artificial': [
                 "PE100058",
                 "MA000001",
             ],
                'future_bwd_summary': [
                 "USE00145_low",
                 "USE00145_high",
                 "USE00145_mean"

             ]
             }

#保留特征列表

features_list = ["S5806281", "S5806282", "S5807322", "S5807323", "S5806058",
                 "S5808597", "S0116880", "S0068143", "S0029752", "S0164358",
                 "S5806052", "S0049507", "S0049493", "S0181392", "S0203259",
                 "S0203260", "M0086399", "USE00020", "PE100058","MA000001","price_open",
                 "price_high","price_low", "price_close", "d111", "d112",
                 "d211", "d221", "d222", "d511", "d512","QA",
                 "MA5", "MA10", "MA15"]

# "USE00145_low", "USE00145_high","USE00145_mean",
#                  "S0049493_2", "S0049493_3", "S0049493_4", "S0029752_2",
#                  "S0029752_3", "S0029752_4"



