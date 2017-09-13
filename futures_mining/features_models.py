#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-12
特征工程
@author: zhoucuilian
"""


from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE



def feature_RFE(trian_x, trian_y):
    """
    返回rank:用标签1标识选中的特征
    """
    cfr = LogisticRegression()
    cfr.fit(trian_x, trian_y)
    rank = []

    for n in range(2, trian_x.shape[1], 1):
        selector = RFE(cfr, n_features_to_select=n, step=1)
        selector.fit(trian_x, trian_y)
        rank.append(selector.ranking_)

    return rank
