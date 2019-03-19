import csv
import os
import pandas as pd

path = 'input/daily'
files = [i[2] for i in os.walk(path)][0]
for i, file in enumerate(files[:-12]):
    basic_filename = path + '/' + file
    basic_stocks = pd.read_csv(basic_filename,encoding='utf_8_sig')
    columns = basic_stocks.columns.tolist()
    if 'target' in columns:
        drop_columns = columns[columns.index('target'):]
        basic_stocks.drop(drop_columns,axis=1,inplace=True)
    if 'close_y' in columns:
        basic_stocks.drop(['close_y'],axis=1,inplace=True)
        basic_stocks.rename(columns={'close_x': 'close'}, inplace=True)
    if 'pct_chg_x' in columns:
        basic_stocks.rename(columns={'pct_chg_x': 'pct_chg'}, inplace=True)
    basic_stocks.to_csv(basic_filename,index=False,encoding='utf_8_sig')
    print('{0} is tag successfully!'.format(file))
