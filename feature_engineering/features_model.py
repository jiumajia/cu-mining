#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-09-12
特征工程
@author: zhoucuilian
"""

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from feature_preprocess.features_gear import features_list
from mining.predict_models import run_model

def feature_RFE(trian_x, trian_y):
    """
    返回rank:用标签1标识选中的特征
    """
    # cfr = LogisticRegression()
    cfr = RandomForestClassifier()
    cfr.fit(trian_x, trian_y)
    rank = []

    for n in range(2, trian_x.shape[1], 1):
        selector = RFE(cfr, n_features_to_select=n, step=1)
        selector.fit(trian_x, trian_y)
        rank.append(selector.ranking_)

    return rank


def run_singlemodel(train_x, trian_y, test_x, test_y):

    rank = feature_RFE(train_x, trian_y)
    for i in range(0, len(rank)):
        index = [x for x in range(0, len(rank[i])) if rank[i][x]==1]
        print [features_list[x] for x in index]
        train = train_x[:, index]
        test = test_x[:, index]
        # step3 ：minning
        ensemble = ['RandomForest']
        run_model(ensemble, train, trian_y, test, test_y)

    return rank



