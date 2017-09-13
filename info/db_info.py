#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-07-25

@author: zhoucuilian
"""
from sqlalchemy import create_engine


# 初始化数据库连接:
alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.140:20306/alpha')

#alpha_con = create_engine('mysql+pymysql://exingcai:uscj!@#@172.16.88.163:20306/alpha')



