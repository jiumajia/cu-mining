from data_handle.table_from_mysql import CuDatafrom feature_preprocess.features_pre import get_pre_datafrom sklearn.model_selection import train_test_splitdef run_data():    """ """    cu = CuData(source="FILE")    train_data, target_data = get_pre_data(cu.data)    train_x, train_y, test_x, test_y = train_test_split(train_data, target_data, test_size=0.2, random_state=42)    return train_x, test_x, train_y, test_y