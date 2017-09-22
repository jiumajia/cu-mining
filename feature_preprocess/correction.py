#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@date: 2017-08-10

@author: zhoucuilian
"""
from __future__ import  division
import pandas as pd
import numpy as np
from scipy import stats
from prettytable import PrettyTable



def get_statics(df,y):
    """
    打印 相关系数信息
    """
    table = PrettyTable(["col_name", "pearsonr","spearmanr"])

    a = np.array(y).tolist()
    a = [float(i) for i in a ]
    for name in df:
        b = np.array(df[name]).tolist()
        b = [float(i) for i in b ]
        r_p = stats.pearsonr(a,b)
        s_p = stats.spearmanr(df[name],y)
        table.add_row([name,round(r_p[0],6),round(s_p[0],6)])



if __name__ == "__main__":
    data = pd.read_csv("../datafiles/cu.csv")
    data = data.drop('date',axis=1)
    data = data.dropna()
    a = pd.DataFrame()
    a["S0181392"] = data["S0181392"].diff(-1)
    a.loc[a['S0181392']>=0,"S0181392"] = 0
    a.loc[a['S0181392']<0,"S0181392"] = -1
    get_statics(data[:-1],a['S0181392'].dropna())
    get_statics(data[:-1],data["S0181392"].diff(-1).dropna())




