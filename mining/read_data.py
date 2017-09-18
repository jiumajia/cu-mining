#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-18

@author: zhoucuilian
"""
from table_from_mysql import Cu_Data
from info.table_info import table_col_map

def read_data():
    try:
        cu = Cu_Data(table_col_map)
        cu.read_data()
        data = cu.get_dataset()

    except Exception,e:
        print e.message

    return data

