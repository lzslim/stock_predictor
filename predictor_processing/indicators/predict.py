import pandas as pd
import numpy as np
import xgboost as xgb
import datetime
from util import *

stocks = pd.read_csv('../../result/all_data.csv',encoding='utf_8_sig')
ts_code = stocks['ts_code']
stocks.drop(['ts_code'],axis=1,inplace=True)
trade_date = stocks['trade_date']
stocks.drop(['trade_date'],axis=1,inplace=True)
dtest = xgb.DMatrix(stocks)

# xgb_model
bst = xgb.Booster()
bst.load_model('../../model/xgb_indicators_20190401.model')
ypred_prob = bst.predict(dtest)

result = pd.DataFrame()
result['predict_prob'] = pd.Series(ypred_prob).astype('float64')
ypred = ypred_prob.round()
result['predict'] = pd.Series(ypred).astype('int64')
result['ts_code'] = ts_code
result['trade_date'] = trade_date
#end_date = getSomeDay(day=3).strftime("%Y%m%d")
end_date = datetime.date.today().strftime("%Y%m%d")
path = '../../result/result_' + end_date + '.csv'
result.to_csv(path,index=False)


# all_xgb_model
bst = xgb.Booster()
bst.load_model('../../model/all_xgb_indicators_20190401.model')
ypred_prob = bst.predict(dtest)

result = pd.DataFrame()
result['predict_prob'] = pd.Series(ypred_prob).astype('float64')
ypred = ypred_prob.round()
result['predict'] = pd.Series(ypred).astype('int64')
result['ts_code'] = ts_code
result['trade_date'] = trade_date
#end_date = getSomeDay(day=3).strftime("%Y%m%d")
end_date = datetime.date.today().strftime("%Y%m%d")
path = '../../result/all_result_' + end_date + '.csv'
result.to_csv(path,index=False)