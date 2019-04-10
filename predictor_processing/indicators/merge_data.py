import pandas as pd
import numpy as np
import csv
import os
import datetime
from util import *

path = '../../result/predictor'
files = [i[2] for i in os.walk(path)][0]
for i, file in enumerate(files):
    filename = path + '/' + file
    if i == 0:
        stocks = pd.read_csv(filename,encoding='utf_8_sig')
    else:
        _next = pd.read_csv(filename,encoding='utf_8_sig')
        stocks = stocks.append(_next,ignore_index=True)
    print('{0} is merged successfully!'.format(file))
trade_date = datetime.date.today().strftime("%Y%m%d")
#trade_date = getSomeDay(day=3).strftime("%Y%m%d")
stocks = stocks[stocks['trade_date'] == int(trade_date)]
stocks.to_csv('../../result/all_data.csv',index=False,encoding='utf_8_sig')