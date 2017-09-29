#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn.ensemble import BaggingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def Bagging(train_x, train_y, test_x, test_y):
    n_estimators_range = [x for x in range(10, 100)]
    accuracy = 0
    iter_num = 0
    start = time.clock()
    for n in n_estimators_range:
        iter_num += 1
        cfr = BaggingClassifier(LogisticRegression(), n_estimators=n,
                                max_samples=0.5, max_features=0.5)
        cfr.fit(train_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(p_out, test_y)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
    end = time.clock()
    print 'svm --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    return accuracy