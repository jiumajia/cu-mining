from data_handle.table_from_mysql import CuDatafrom feature_preprocess.features_pre import get_pre_datafrom sklearn.model_selection import train_test_splitfrom feature_engineering.features_model import run_singlemodelfrom mining.Xgboost import run_xgboostdef run_data():    """ """    data_start_date = '2016-01-01'    data_end_date = '2017-7-30'    cu = CuData(start_date=data_start_date, end_date=data_end_date,source="DB")    train_data, target_data = get_pre_data(cu.data)    train_x, train_y, test_x, test_y = train_test_split(train_data, target_data, test_size=0.2, random_state=42)    return train_x, test_x, train_y, test_yif __name__ == "__main__":    train_x, test_x, train_y, test_y = run_data()    print train_x.shape    run_singlemodel(train_x, test_x, train_y, test_y)    # run_xgboost(train_x, test_x, train_y, test_y)