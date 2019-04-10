import csv
import os
import pandas as pd
from util import *

PERIOD = 8
path = 'input/daily'
files = [i[2] for i in os.walk(path)][0]
for i, file in enumerate(files[:-9]):
    basic_filename = path + '/' + file
    basic_stocks = pd.read_csv(basic_filename,encoding='utf_8_sig')
    columns = basic_stocks.columns.tolist()
    if 'target' in columns:
        basic_stocks.drop(['target'],axis=1,inplace=True)
    for j in range(PERIOD):
        filename = path + '/' + files[i+j+1]
        if j == 0:
            stocks = pd.read_csv(filename,encoding='utf_8_sig',usecols = [0,10])
            stocks.rename(columns={'pct_chg': 'pct_chg_period'}, inplace=True)
            stocks['target'] = 0
        else:
            nextday_stocks = pd.read_csv(filename,encoding='utf_8_sig',usecols = [0,10])
            stocks = pd.merge(stocks,nextday_stocks,how='right',on='ts_code')
            stocks.drop(['pct_chg'],axis=1,inplace=True)
            stocks['pct_chg_period'] = stocks['pct_chg_period'] + nextday_stocks['pct_chg']
            stocks['target'] = stocks.apply(lambda x: check_target(x['pct_chg_period'],x['target']), axis=1)
    stocks.drop(['pct_chg_period'],axis=1,inplace=True)
    basic_stocks = pd.merge(basic_stocks,stocks,how='left',on='ts_code')
    basic_stocks.dropna()
    basic_stocks.to_csv(basic_filename,index=False,encoding='utf_8_sig')
    print('{0} is tag successfully!'.format(file))
