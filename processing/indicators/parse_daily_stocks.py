import pandas as pd
import numpy as np
import csv
import os

# 合并所有数据
path = '../../input/daily'
files = [i[2] for i in os.walk(path)][0]

for i, file in enumerate(files[:-12]):
    filename = path + '/' + file
    if i == 0:
        stocks = pd.read_csv(filename,encoding='utf_8_sig')
    else:
        _next = pd.read_csv(filename,encoding='utf_8_sig')
        stocks = stocks.append(_next,ignore_index=True)
    print('{0} is merged successfully!'.format(file))

stocks = stocks.sort_values(['ts_code','trade_date_x'],ascending=[True,False])
ts_code_set = set(stocks['ts_code'].tolist())
path = '../../input/stocks'
for ts_code in ts_code_set:
    stock_df = stocks[stocks['ts_code'] == ts_code]
    if stock_df.shape[0] > 30:
        new_path = '../../input/stocks/' + ts_code.split('.')[0] + '.csv'
        if 'trade_date_y' in stock_df.columns.tolist():
            stock_df.drop(['trade_date_y'],axis=1,inplace=True)
            stock_df.rename(columns={'trade_date_x': 'trade_date'}, inplace=True)
            stock_df.to_csv(new_path,index=False,encoding='utf_8_sig')
        print('{0} is parsed successfully!'.format(ts_code))

