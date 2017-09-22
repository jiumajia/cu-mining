#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def NaiveBayes(tran_x, train_y, test_x, test_y):
    accuracy = 0
    iter_num = 0
    start = time.clock()
    cfr = GaussianNB()
    cfr.fit(tran_x, train_y)
    p_out = cfr.predict(test_x)
    accuracy_t = accuracy_score(test_y, p_out)
    if (accuracy < accuracy_t):
        accuracy = accuracy_t
        params = cfr.get_params()
    end = time.clock()
    print 'NaiveBayes --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    return accuracy