#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def RandomForest(tran_x, train_y, test_x, test_y):
    accuracy = 0
    n_estimators_range = [x for x in range(10, 100)]
    criterion = ['gini', 'entropy']

    # step1:training svm,save optimal parameter
    iter_num = 0
    start = time.clock()
    for c in criterion:
        for n in n_estimators_range:
            iter_num += 1
            cfr = RandomForestClassifier(n_estimators=n, criterion=c)
            cfr.fit(tran_x, train_y)
            p_out = cfr.predict(test_x)
            accuracy_t = accuracy_score(test_y, p_out)
            if (accuracy < accuracy_t):
                accuracy = accuracy_t
                params = cfr.get_params()

    end = time.clock()
    print 'RandomForest --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    return accuracy