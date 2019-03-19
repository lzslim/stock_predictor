import pandas as pd
import numpy as np
import csv
import os
from trendline import *

path = '../../input/stocks'
files = [i[2] for i in os.walk(path)][0]

for i, file in enumerate(files):
    filename = path + '/' + file
    stocks = pd.read_csv(filename,encoding='utf_8_sig')
    # ema
    new_stocks = ema(stocks)
    # macd
    new_stocks = pd.merge(new_stocks,macd(stocks),how='left',on='trade_date')
    # kdj
    new_stocks = pd.merge(new_stocks,kdj(stocks),how='left',on='trade_date')
    # rsi
    new_stocks = pd.merge(new_stocks,rsi(stocks),how='left',on='trade_date')
    # vrsi
    new_stocks = pd.merge(new_stocks,vrsi(stocks),how='left',on='trade_date')
    # boll
    new_stocks = pd.merge(new_stocks,boll(stocks),how='left',on='trade_date')
    # wr
    new_stocks = pd.merge(new_stocks,wr(stocks),how='left',on='trade_date')
    # bias
    new_stocks = pd.merge(new_stocks,bias(stocks),how='left',on='trade_date')
    # asi
    new_stocks = pd.merge(new_stocks,asi(stocks),how='left',on='trade_date')
    # vr_rate
    new_stocks = pd.merge(new_stocks,vr_rate(stocks),how='left',on='trade_date')
    # arbr
    new_stocks = pd.merge(new_stocks,arbr(stocks),how='left',on='trade_date')
    # dpo
    new_stocks = pd.merge(new_stocks,dpo(stocks),how='left',on='trade_date')
    # trix
    new_stocks = pd.merge(new_stocks,trix(stocks),how='left',on='trade_date')
    # mtm
    new_stocks = pd.merge(new_stocks,mtm(stocks),how='left',on='trade_date')
    # obv
    new_stocks = pd.merge(new_stocks,obv(stocks),how='left',on='trade_date')
    # cci
    new_stocks = pd.merge(new_stocks,cci(stocks),how='left',on='trade_date')
    # priceosc
    new_stocks = pd.merge(new_stocks,priceosc(stocks),how='left',on='trade_date')
    # others
    new_stocks = pd.merge(new_stocks,stocks[['trade_date','turnover_rate','target']],how='left',on='trade_date')

    new_stocks.replace('', np.nan, inplace=True)
    new_stocks.dropna(inplace=True)
    new_file = '../../input/train_data/' + file
    new_stocks.to_csv(new_file,index=False,encoding='utf_8_sig')
    print('{0} is pretrain successfully!'.format(file))


    