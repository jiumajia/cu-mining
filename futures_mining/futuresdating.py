# -*- coding: utf-8 -*-
import pandas as pd

def Fdating(df, format_dic):
    # parameters :
    # df is pandas DataFrame
    # feature_names is a list like ['S0164358':2,'S01643532':3,...]
    # return DataFrame will add new feature with addition of times columns corresponding to features

    # parameters' check
    if not isinstance(df, pd.DataFrame):
        return "please using pandas.DataFrame as first parameter"

    try:
        for name in format_dic.keys():
            df[name]
    except KeyError:
        return "KeyError, feature name is not in DataFrame :" + name

    # Set feature 'target' to first column
    try:
        pop_data = df.pop('target')
        df.insert(0, 'target', pop_data)
    except Exception, e:
        return e
    #
    try:
        for name, values in format_dic.items():
            for value in values:
                temp = []   # set a temp list to store dating field
                dating_list = []  # using list to store times of rows : [1,2,3]..if new row 5-> 1(pop)..[2,3,5]

                for row_num in range(len(df[name])):

                    if len(dating_list) < value - 1:
                        dating_list.append(df[name][row_num])
                        temp.append(0)
                    else:
                        dating_list.append(df[name][row_num])
                        temp.append(sum(dating_list))
                        dating_list.pop(0)
                new_col_name = "%s_%s" % (name, value)
                df[new_col_name] = temp
    except Exception, e:
        return e

    return df

if __name__ == "__main__":
    # example
    aa = {'one': [1, 2, 3, 4], 'two': [11, 12, 13, 14], 'target': [5, 6, 7, 8]}
    df = pd.DataFrame(aa)
    print Fdating(df, {'two': 2, 'one': 3})
#
#     result:
#    target  one  two  two_2  one_3
# 0       5    1   11      0      0
# 1       6    2   12     23      0
# 2       7    3   13     25      6
# 3       8    4   14     27      9