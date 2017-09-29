#!/usr/bin/env python# -*- coding: utf-8 -*-from feature_preprocess.dummy_features import Fdatingimport talibimport pandas as pdimport datetimeimport numpy as npimport sysdef get_day(date):    """        :return: day = 1,2,3,....30    """    if not isinstance(date, datetime.datetime):       date = datetime.datetime.strptime(date, "%Y-%m-%d")    query_day = int("%s" % (date.strftime("%d")))    return query_daydef get_quarter(date):    """        :return: QA = 1,2,3,or 4    """    if not isinstance(date, datetime.datetime):       date = datetime.datetime.strptime(date, "%Y-%m-%d")    query_month = int("%s" % (date.strftime("%m")))    QA = query_month % 3 + 1    return QAF_STAG1 = ["S5806281", "S5806282", "S5807322", "S5807323", "S5806058",                 "S5808597", "S0116880", "S0068143", "S0029752", "S0164358",                 "S5806052", "S0049507", "S0049493", "S0181392", "S0203259",                 "S0203260", "M0086399", "USE00020", "PE100058", "MA000001",                 "price_open", "price_close", "MA5", "MA10", "MA15",                  "d111", "d112", "d211", "d221", "d222", "d511", "d512", "QA", "PE100042"                 ]F_STAG2 = ["S0181392", "S5806281", "S5806282", "S5806058",                    "S5808597", "S0116880", "S0049493", "S0203259", "S0068143", "S0029752",                    "price_open", "price_high", "price_low", "price_close",                    "S5806052", "S0049507", "S0164358", "S0203260", "M0086399", "d111", "d112",                    "d211", "d512", "d522", "d611", "d612", "target"]features_list = F_STAG2# features_list = ["S5806281", "S5806282", "S5807322", "S5807323", "S5806058",#                  "S5808597", "S0116880", "S0068143", "S0029752", "S0164358",#                  "S5806052", "S0049507", "S0049493", "S0181392", "S0203259",#                  "S0203260", "M0086399", "USE00020",#                  "price_open", "price_close",#                   "d111", "d112", "d211", "d221", "d222", "d511", "d512", "QA", "target"#                  ]def f_stage_one(dataset):    #feature    p_data = pd.DataFrame()    # D111: 期货结算价 ：  期货结算价(连续):阴极铜 - 期货结算价(连三):阴极铜    p_data['d111'] = abs(dataset['S0068143'] - dataset['S0116880'])    # D112: 长江有色升贴水 ： (铜升贴水:最小值:长江有色市场 + 铜升贴水:最大值:长江有色市场) /2    p_data['d112'] = (dataset['S5806281'] + dataset['S5806282'])/2    # # D121: LME铜升贴水(0-3)    # p_data['d121'] = self.dataset['S5806058']    # # D122: LME铜升贴水(3-15)    # p_data['d122'] = self.dataset['S5808597']    # D123: (最低溢价:上海电解铜:保税库(仓单) + 最高溢价:上海电解铜:保税库(仓单)) / 2    #p_data['d123'] = (self.dataset['S5807322'] + self.dataset['S5807323'])/2    # D211: LME仓单比例 ：  LME铜:注册仓单:合计:全球 / 总库存:LME铜    p_data['d211'] = (dataset['S0164358'] / dataset['S0029752'])/2    # D212 ： LME总库存： 总库存:LME铜    #p_data['S0029752'] = self.dataset['S0029752']    # D221: 国内仓单比例 ： 持仓仓单 / 库存小计:阴极铜:总计    p_data['d221'] = (dataset['S0049493'] / dataset['S0049507'])/2    # D222: 国内库存： 库存小计:阴极铜:总计    p_data['d222'] = dataset['S0049507']    # D511: LME铜持仓量 * 25（吨 / 手）    p_data['d511'] = dataset['S5806052'] * 25    # D512: 持仓比; LME铜持仓量 * 25（吨 / 手） / 总库存    p_data['d512'] = (dataset['S5806052'] * 25 /dataset['S0029752']) / 2    # D521: 国内持仓量 / 2 * 5(吨 / 手)    p_data['d521'] = dataset['M0086399'] / 2 * 5    # D522: 国内持仓比： 国内持仓量 / 2 * 5(吨 / 手) / 总库存    p_data['d522'] = (dataset['M0086399'] / 2 * 5 / dataset['S0049507'])    # D611: 升贴水差值： 铜升贴水:最大值:长江有色市场 - 铜升贴水:最小值:长江有色市场    p_data['d611'] = dataset['S5806282'] - dataset['S5806281']    # D612: 1 # 铜升贴水:最大值:上海金属 - 1#铜升贴水:最小值:上海金属    p_data['d612'] = dataset['S0203260'] - dataset['S0203259']    p_data['d711'] = dataset['PE100058'] / dataset['MA000001']    p_data['d712'] = dataset['S0049493'] / dataset ['MA000001']    #p_data['date'] = self.dataset['date']    p_data['S0049493'] = dataset['S0049493']    p_data['price_open'] = dataset['price_open']    p_data['price_high'] = dataset['price_high']    p_data['price_low'] = dataset['price_low']    p_data['price_close'] = dataset['price_close']    p_data['MA2'] = talib.MA(p_data['price_close'].values, timeperiod=2)  #调用talib计算5日均线的值    p_data['MA3'] = talib.MA(p_data['price_close'].values, timeperiod=3)    p_data['MA4'] = talib.MA(p_data['price_close'].values, timeperiod=4)    p_data['MA5'] = talib.MA(p_data['price_close'].values, timeperiod=5)  #调用talib计算5日均线的值    p_data['MA6'] = talib.MA(p_data['price_close'].values, timeperiod=6)    p_data['MA10'] = talib.MA(p_data['price_close'].values, timeperiod=10)    p_data['MA15'] = talib.MA(p_data['price_close'].values, timeperiod=15)    #p_data['MA20'] = talib.MA(p_data['price_close'].values, timeperiod=20)    #p_data['EMA20'] = talib.EMA(p_data['price_close'].values, timeperiod=20)    p_data['QA'] = dataset['date'].map(get_quarter)    p_data['day'] = dataset['date'].map(get_day)    #index    # print dataset    dataset = pd.merge(dataset, p_data, how='outer')    dataset = pd.concat([dataset], ignore_index=True)    dic = {'S0049493': [2, 3, 4], 'S0029752': [2, 3, 4]}    dataset = Fdating(dataset, dic)    # OUT dataset    dataset = dataset[features_list]    # Delete nan    dataset = dataset.dropna(axis=0)    # Set train    train_data = np.array(dataset[features_list[:-1]])    # np.savetxt('D:/cu-final.csv', train_data, delimiter=',')    # Set target    target_data = np.array(dataset['target'])    return train_data, target_datadef f_stage_two(dataset):    dataset['S0049507'] = dataset['S0049507'].fillna(method='bfill')    dataset = dataset.dropna(subset=['S0181392'])    dataset = dataset.drop(['S5807322', 'S5807323', 'USE00020'], axis=1)    dataset['d111'] = abs(dataset['S0068143'] - dataset['S0116880'])    dataset['d112'] = (dataset['S5806281'] + dataset['S5806282'])/2    dataset['d211'] = (dataset['S0164358'] / dataset['S0029752'])/2    dataset['d221'] = (dataset['S0049493'] / dataset['S0049507'])/2    dataset['d512'] = (dataset['S5806052'] * 25 / dataset['S0029752']) / 2    dataset['d522'] = (dataset['M0086399'] / 2 * 5 / dataset['S0049507'])    dataset['d611'] = dataset['S5806282'] - dataset['S5806281']    dataset['d612'] = dataset['S0203260'] - dataset['S0203259']    dataset = dataset[features_list]    dataset = dataset.dropna()    print (len(dataset))    train_data = np.array(dataset[features_list[:-1]])    target_data = np.array(dataset['target'])    return train_data, target_datadef set_features(dataset, stage="f_stage_one"):    func = getattr(sys.modules[__name__], stage)    return func(dataset)