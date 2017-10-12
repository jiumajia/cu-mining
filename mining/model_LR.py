#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def Linear(train_x, train_y, test_x, test_y):
    solver = ['liblinear', 'newton-cg', 'sag', 'lbfgs']
    # step1:training svm,save optimal parameter
    iter_num = 0
    start = time.clock()
    accuracy = 0
    for s in solver:
        iter_num += 1
        cfr = LogisticRegression(solver=s)
        cfr.fit(train_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(test_y, p_out)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
            out = p_out
    end = time.clock()
    print 'LR --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    print len(out)
    return cfr