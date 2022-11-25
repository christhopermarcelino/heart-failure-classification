import numpy as np
import pandas as pd
import joblib
from os.path import join, dirname, realpath

LE_EXERCISEANGINA_PATH = join(dirname(realpath(__file__)), '../models/label_encoder_exerciseangina.joblib')
LE_SEX_PATH = join(dirname(realpath(__file__)), '../models/label_encoder_sex.joblib')
OHE_PATH = join(dirname(realpath(__file__)), '../models/one_hot_encoder.joblib')

def feature_engineering(data):
    data = label_encoding(data)
    data = one_hot_encoding(data)

    return data

def label_encoding(data):
    label_encoder_exerciseangina = joblib.load(LE_EXERCISEANGINA_PATH)
    label_encoder_sex = joblib.load(LE_SEX_PATH)

    data['exerciseangina'] = label_encoder_exerciseangina.transform(data['exerciseangina'])
    data['sex'] = label_encoder_sex.transform(data['sex'])

    return data

def one_hot_encoding(data):
    categorical_column_to_one_hot_encode = ['st_slope', 'restingecg', 'chestpaintype']

    one_hot_encoder = joblib.load(OHE_PATH)

    temp = [
        ['Up', 'ASY', 'LVH']
    ]

    # print(data[categorical_column_to_one_hot_encode])

    feature_arr = one_hot_encoder.transform(temp).toarray()
    # feature_arr = one_hot_encoder.transform(data[categorical_column_to_one_hot_encode]).toarray()
    feature_labels = one_hot_encoder.categories_

    feature_labels = list(np.concatenate(feature_labels))

    features = pd.DataFrame(feature_arr, columns=feature_labels)

    data.drop(columns=categorical_column_to_one_hot_encode, inplace=True)

    data = pd.concat([data, features], axis=1)

    return data
