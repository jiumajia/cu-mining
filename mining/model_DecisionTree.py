#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

def DecisionTree(train_x, train_y, test_x, test_y):
    accuracy = 0
    criterion = ['gini', 'entropy']
    iter_num = 0

    for c in criterion:
        iter_num += 1
        start = time.clock()
        cfr = DecisionTreeClassifier(criterion=c)
        cfr.fit(train_x, train_y)
        p_out = cfr.predict(test_x)
        accuracy_t = accuracy_score(test_y, p_out)
        if (accuracy < accuracy_t):
            accuracy = accuracy_t
            params = cfr.get_params()
    end = time.clock()
    print 'DecisionTree --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    return accuracy