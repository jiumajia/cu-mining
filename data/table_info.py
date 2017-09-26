#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""

# table_name = {'data_wind', 'future_exchange', 'data_sina_day_kline','future_bwd_summary','data_artificial'}

table_col_map = {
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
                # "MA000001",
             ],
             #    'future_bwd_summary': [
             #     "USE00145_low",
             #     "USE00145_high",
             #     "USE00145_mean"
             #
             # ],

                'preprocess_day_position_chain': [
                 "PE100042"
             ]
             }

#保留特征列表

features_list = ["S5806281", "S5806282", "S5807322", "S5807323", "S5806058",
                 "S5808597", "S0116880", "S0068143", "S0029752", "S0164358",
                 "S5806052", "S0049507", "S0049493", "S0181392", "S0203259",
                 "S0203260", "M0086399", "USE00020", "PE100058","price_open","price_close",
                 "MA5","MA10","MA15",
                  "d111", "d112","d211", "d221", "d222", "d511", "d512","QA","PE100042"
                 ]

# "USE00145_low", "USE00145_high","USE00145_mean",
#                  "S0049493_2", "S0049493_3", "S0049493_4", "S0029752_2",
#                  "S0029752_3", "S0029752_4"

    #
    #
    # 'day_preprocess': [
    #              "PE100035",
    #              "PE100036"
    #          ],