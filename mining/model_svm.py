#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sklearn import svm
from sklearn.metrics import accuracy_score

def SVM(train_x, train_y, test_x, test_y):
    gamma_2d_range = [x * 0.01 for x in range(2, 30)]
    C_2d_range = [x for x in range(2, 30)]
    kernel_function = ['rbf', 'poly', 'sigmoid']

    # step1:training svm,save optimal parameter
    start = time.clock()
    iter_num = 0
    accuracy = 0
    for svm_k in kernel_function:
        for svm_c in C_2d_range:
            for svm_g in gamma_2d_range:
                iter_num += 1
                cfr = svm.SVC(kernel=svm_k, C=svm_c, gamma=svm_g)
                cfr.fit(train_x, train_y)
                p_out = cfr.predict(test_x)
                accuracy_t = accuracy_score(test_y, p_out)
                if (accuracy < accuracy_t):
                    accuracy = accuracy_t
                    params = cfr.get_params()

    end = time.clock()
    print 'svm --- ', ' iterations', iter_num, ' run time:', end - start

    # 打印最优参数列表
    print '精确率', accuracy, '参数列表', params
    return accuracy
