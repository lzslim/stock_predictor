import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score,roc_auc_score,accuracy_score
from sklearn.metrics import roc_curve, auc, recall_score, precision_score
import matplotlib.pyplot as plt
import xgboost as xgb
from operator import itemgetter
import datetime


stocks = pd.read_csv('result/all_data.csv',encoding='utf_8_sig')
ts_code = stocks['ts_code']
stocks.drop(['trade_date'],axis=1,inplace=True)


bst = xgb.Booster()
bst.load_model('./model/xgb_indicators_20190325.model')

print('Predicting ...')
check = bst.predict(X_dtest)
check2 = check.round()

print('Merging ...')




