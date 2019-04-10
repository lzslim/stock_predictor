import pandas as pd
import numpy as np
from util import *
import os

path = '../../input/stocks'
files = [i[2] for i in os.walk(path)][0]
PERIOD = 9

for i, file in enumerate(files):
    filename = path + '/' + file
    stocks = pd.read_csv(filename,encoding='utf_8_sig')
    stocks.drop(['target'],axis=1,inplace=True)
    stocks['target'] = tag(stocks['pct_chg'],PERIOD)
    print(filename)
    stocks.to_csv(filename,index=False,encoding='utf_8_sig')
    exit()