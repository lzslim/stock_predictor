import pandas as pd
import numpy as np
import csv
import os

path = '../../input/train_data'
files = [i[2] for i in os.walk(path)][0]
for i, file in enumerate(files):
    filename = path + '/' + file
    if i == 0:
        stocks = pd.read_csv(filename,encoding='utf_8_sig')
    else:
        _next = pd.read_csv(filename,encoding='utf_8_sig')
        stocks = stocks.append(_next,ignore_index=True)
    print('{0} is merged successfully!'.format(file))
stocks = stocks.sort_values(['trade_date'])
stocks.to_csv('../../input/all_data.csv',index=False,encoding='utf_8_sig')