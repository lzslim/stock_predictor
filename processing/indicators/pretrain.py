import pandas as pd
import numpy as np
import csv
import os
from trendline import *
from util import *

path = '../../input/stocks'
files = [i[2] for i in os.walk(path)][0]

for i, file in enumerate(files):
    try:
        filename = path + '/' + file
        stocks = pd.read_csv(filename,encoding='utf_8_sig')
        stocks = stocks.sort_values(['trade_date'])
        old_features = list(stocks.columns.values)
        old_features.remove('trade_date')
        old_features.remove('pe')
        old_features.remove('ps')
        old_features.remove('ts_code')

        # ema
        # new_stocks = ema(stocks)
        # vrsi
        new_stocks = vrsi(stocks)
        # ma_10
        #new_stocks = pd.merge(new_stocks,ma(stocks,n=10),how='left',on='trade_date')
        # ma_5
        #new_stocks = pd.merge(new_stocks,ma(stocks,n=5),how='left',on='trade_date')
        # macd
        #new_stocks = pd.merge(new_stocks,macd(stocks),how='left',on='trade_date')
        # kdj
        new_stocks = pd.merge(new_stocks,kdj(stocks),how='left',on='trade_date')
        # rsi
        new_stocks = pd.merge(new_stocks,rsi(stocks),how='left',on='trade_date')
        # boll
        #new_stocks = pd.merge(new_stocks,boll(stocks),how='left',on='trade_date')
        # wr
        # new_stocks = pd.merge(new_stocks,wr(stocks),how='left',on='trade_date')
        # bias_20
        new_stocks = pd.merge(new_stocks,bias(stocks,n=20),how='left',on='trade_date')
        # bias_10
        new_stocks = pd.merge(new_stocks,bias(stocks,n=10),how='left',on='trade_date')
        # bias_5
        new_stocks = pd.merge(new_stocks,bias(stocks,n=5),how='left',on='trade_date')
        # asi
        #new_stocks = pd.merge(new_stocks,asi(stocks),how='left',on='trade_date')
        # mi
        #new_stocks = pd.merge(new_stocks,mi(stocks),how='left',on='trade_date')
        # # jdqs
        # #new_stocks = pd.merge(new_stocks,jdqs(stocks),how='left',on='trade_date')
        # # up_n
        new_stocks = pd.merge(new_stocks,up_n(stocks),how='left',on='trade_date')
        # down_n
        new_stocks = pd.merge(new_stocks,down_n(stocks),how='left',on='trade_date')
        # vr_rate
        new_stocks = pd.merge(new_stocks,vr_rate(stocks),how='left',on='trade_date')
        # arbr
        new_stocks = pd.merge(new_stocks,arbr(stocks),how='left',on='trade_date')
        # dpo
        #new_stocks = pd.merge(new_stocks,dpo(stocks),how='left',on='trade_date')
        # trix
        new_stocks = pd.merge(new_stocks,trix(stocks),how='left',on='trade_date')
        # mtm
        #new_stocks = pd.merge(new_stocks,mtm(stocks),how='left',on='trade_date')
        # obv
        new_stocks = pd.merge(new_stocks,obv(stocks),how='left',on='trade_date')
        # cci
        #new_stocks = pd.merge(new_stocks,cci(stocks),how='left',on='trade_date')
        # mfi
        #new_stocks = pd.merge(new_stocks,mfi(stocks),how='left',on='trade_date')
        # adtm
        #new_stocks = pd.merge(new_stocks,adtm(stocks),how='left',on='trade_date')
        # micd
        #new_stocks = pd.merge(new_stocks,micd(stocks),how='left',on='trade_date')

        stocks['f01'] = stocks.close/stocks.open - 1
        stocks['f02'] = stocks.open/stocks.close.shift(1) - 1
        stocks['f03'] = stocks.high/stocks.low - 1
        stocks['f04'] = stocks.low/stocks.high.shift(1) - 1
        stocks['f05'] = stocks.high/stocks.low.shift(1) - 1

        stocks['f06'] = stocks.vol.apply(np.log)
        stocks['f07'] = stocks.amount.apply(np.log)
        stocks['f08'] = stocks.total_share.apply(np.log)
        stocks['f09'] = stocks.float_share.apply(np.log)
        stocks['f10'] = stocks.float_share.apply(np.log)
        stocks['f11'] = stocks.total_mv.apply(np.log)
        stocks['f12'] = stocks.circ_mv.apply(np.log)

        stocks['f13'] = stocks.vol.pct_change(1)
        stocks['f14'] = stocks.vol.pct_change(5)
        stocks['f15'] = stocks.vol.pct_change(20)
        stocks['f16'] = stocks.vol.pct_change(40)
        stocks['f17'] = stocks.vol.pct_change(80)
        stocks['f18'] = stocks.close.pct_change(1)
        stocks['f19'] = stocks.close.pct_change(5)
        stocks['f20'] = stocks.close.pct_change(20)
        stocks['f21'] = stocks.close.pct_change(40)
        stocks['f22'] = stocks.close.pct_change(80)
        stocks['f23'] = stocks.open.pct_change(1)
        stocks['f24'] = stocks.open.pct_change(5)
        stocks['f25'] = stocks.open.pct_change(20)
        stocks['f26'] = stocks.open.pct_change(40)
        stocks['f27'] = stocks.open.pct_change(80)
        stocks['f28'] = stocks.low.pct_change(1)
        stocks['f29'] = stocks.low.pct_change(5)
        stocks['f30'] = stocks.low.pct_change(20)
        stocks['f31'] = stocks.low.pct_change(40)
        stocks['f32'] = stocks.low.pct_change(80)
        stocks['f33'] = stocks.high.pct_change(1)
        stocks['f34'] = stocks.high.pct_change(5)
        stocks['f35'] = stocks.high.pct_change(20)
        stocks['f36'] = stocks.high.pct_change(40)
        stocks['f37'] = stocks.high.pct_change(80)
        stocks['f38'] = stocks.turnover_rate_f.pct_change(1)
        stocks['f39'] = stocks.turnover_rate_f.pct_change(5)
        stocks['f40'] = stocks.turnover_rate_f.pct_change(20)
        stocks['f41'] = stocks.turnover_rate_f.pct_change(40)
        stocks['f43'] = stocks.circ_mv.pct_change(1)
        stocks['f44'] = stocks.circ_mv.pct_change(5)
        stocks['f45'] = stocks.circ_mv.pct_change(20)
        stocks['f46'] = stocks.circ_mv.pct_change(40)
        stocks['f47'] = stocks.circ_mv.pct_change(80)

        stocks['f48'] = ma(stocks.close, 5) 
        stocks['f49'] = ma(stocks.close, 20)
        stocks['f50'] = ma(stocks.close, 40)
        stocks['f51'] = ma(stocks.close, 80)
        stocks['f52'] = ma(stocks.turnover_rate_f, 5)
        stocks['f53'] = ma(stocks.turnover_rate_f, 20)
        stocks['f54'] = ma(stocks.turnover_rate_f, 40)
        stocks['f55'] = ma(stocks.turnover_rate_f, 80)
        stocks['f52'] = ma(stocks.vol, 5).apply(np.log)
        stocks['f53'] = ma(stocks.vol, 20).apply(np.log)
        stocks['f54'] = ma(stocks.vol, 40).apply(np.log)
        stocks['f55'] = ma(stocks.vol, 80).apply(np.log)
        stocks['f56'] = stocks.vol/ma(stocks.vol, 5) - 1
        stocks['f57'] = stocks.vol/ma(stocks.vol, 20) - 1
        stocks['f58'] = stocks.vol/ma(stocks.vol, 40) - 1
        stocks['f59'] = stocks.vol/ma(stocks.vol, 80) - 1
        stocks['f60'] = stocks.turnover_rate_f/ma(stocks.turnover_rate_f, 5) - 1
        stocks['f61'] = stocks.turnover_rate_f/ma(stocks.turnover_rate_f, 20) - 1
        stocks['f62'] = stocks.turnover_rate_f/ma(stocks.turnover_rate_f, 40) - 1
        stocks['f63'] = stocks.turnover_rate_f/ma(stocks.turnover_rate_f, 80) - 1
        stocks['f64'] = stocks.close/ma(stocks.close, 5) - 1
        stocks['f65'] = stocks.close/ma(stocks.close, 5) - 1
        stocks['f66'] = stocks.close/ma(stocks.close, 5) - 1
        stocks['f67'] = stocks.close/ma(stocks.close, 5) - 1
        stocks['f68'] = stocks.vol/ema(stocks.vol,5) - 1
        stocks['f69'] = stocks.vol/ema(stocks.vol,20) - 1
        stocks['f70'] = stocks.vol/ema(stocks.vol,40) - 1
        stocks['f71'] = stocks.vol/ema(stocks.vol,80) - 1
        stocks['f72'] = stocks.close/ema(stocks.close,5) - 1
        stocks['f73'] = stocks.close/ema(stocks.close,20) - 1
        stocks['f74'] = stocks.close/ema(stocks.close,40) - 1
        stocks['f75'] = stocks.close/ema(stocks.close,80) - 1

        stocks['f76'] = zscore_fun(stocks.close,20,10)
        stocks['f77'] = zscore_fun(stocks.close,40,30)
        stocks['f78'] = zscore_fun(stocks.close,80,30)
        stocks['f79'] = zscore_fun(stocks.close,160,30)
        stocks['f80'] = zscore_fun(stocks.vol,20,10)
        stocks['f81'] = zscore_fun(stocks.vol,40,30)
        stocks['f82'] = zscore_fun(stocks.vol,80,30)
        stocks['f83'] = zscore_fun(stocks.vol,160,30)
        stocks['f84'] = zscore_fun(stocks.open,20,10)
        stocks['f85'] = zscore_fun(stocks.open,40,30)
        stocks['f86'] = zscore_fun(stocks.open,80,30)
        stocks['f87'] = zscore_fun(stocks.open,160,30)
        stocks['f88'] = zscore_fun(stocks.low,20,10)
        stocks['f89'] = zscore_fun(stocks.low,40,30)
        stocks['f90'] = zscore_fun(stocks.low,80,30)
        stocks['f91'] = zscore_fun(stocks.low,160,30)
        stocks['f92'] = zscore_fun(stocks.high,20,10)
        stocks['f93'] = zscore_fun(stocks.high,40,30)
        stocks['f94'] = zscore_fun(stocks.high,80,30)
        stocks['f95'] = zscore_fun(stocks.high,160,30)
        
        stocks['f96'] = stocks['f01'].dropna().rank(pct=True)
        stocks['f97'] = stocks['f02'].dropna().rank(pct=True)
        stocks['f98'] = stocks['f03'].dropna().rank(pct=True)
        stocks['f99'] = stocks['f04'].dropna().rank(pct=True)
        stocks['f100'] = stocks['f05'].dropna().rank(pct=True)
        stocks['f101'] = stocks.vol.rank(pct=True)
        stocks['f102'] = stocks['f13'].dropna().rank(pct=True)
        stocks['f103'] = stocks['f14'].dropna().rank(pct=True)
        stocks['f104'] = stocks['f15'].dropna().rank(pct=True)
        stocks['f105'] = stocks['f16'].dropna().rank(pct=True)
        stocks['f106'] = stocks['f17'].dropna().rank(pct=True)
        stocks['f107'] = stocks['f18'].dropna().rank(pct=True)
        stocks['f108'] = stocks['f19'].dropna().rank(pct=True)
        stocks['f109'] = stocks['f20'].dropna().rank(pct=True)
        stocks['f110'] = stocks['f21'].dropna().rank(pct=True)
        stocks['f111'] = stocks['f22'].dropna().rank(pct=True)
        stocks['f107'] = stocks['f18'].dropna().rank(pct=True)
        stocks['f108'] = stocks['f19'].dropna().rank(pct=True)
        stocks['f109'] = stocks['f20'].dropna().rank(pct=True)
        stocks['f110'] = stocks['f21'].dropna().rank(pct=True)
        stocks['f111'] = stocks['f22'].dropna().rank(pct=True)
        stocks['f112'] = stocks['f76'].dropna().rank(pct=True)
        stocks['f113'] = stocks['f77'].dropna().rank(pct=True)
        stocks['f114'] = stocks['f78'].dropna().rank(pct=True)
        stocks['f115'] = stocks['f79'].dropna().rank(pct=True)
        stocks['f116'] = stocks['f80'].dropna().rank(pct=True)
        stocks['f117'] = stocks['f81'].dropna().rank(pct=True)
        stocks['f118'] = stocks['f82'].dropna().rank(pct=True)
        stocks['f119'] = stocks['f83'].dropna().rank(pct=True)

        stocks['f120'] = stocks['f13'].apply(np.sign)
        stocks['f121'] = stocks['f14'].apply(np.sign)
        stocks['f122'] = stocks['f15'].apply(np.sign)
        stocks['f123'] = stocks['f16'].apply(np.sign)
        stocks['f124'] = stocks['f17'].apply(np.sign)
        stocks['f125'] = stocks['f18'].apply(np.sign)
        stocks['f126'] = stocks['f19'].apply(np.sign)
        stocks['f127'] = stocks['f20'].apply(np.sign)
        stocks['f128'] = stocks['f21'].apply(np.sign)
        stocks['f129'] = stocks['f22'].apply(np.sign)

        stocks['f130'] = plus_minus_fxn(stocks['f120'],20)
        stocks['f131'] = plus_minus_fxn(stocks['f120'],40)
        stocks['f132'] = plus_minus_fxn(stocks['f121'],20)
        stocks['f133'] = plus_minus_fxn(stocks['f121'],40)
        stocks['f134'] = plus_minus_fxn(stocks['f122'],20)
        stocks['f135'] = plus_minus_fxn(stocks['f122'],40)
        stocks['f136'] = plus_minus_fxn(stocks['f123'],20)
        stocks['f137'] = plus_minus_fxn(stocks['f123'],40)
        stocks['f138'] = plus_minus_fxn(stocks['f124'],20)
        stocks['f139'] = plus_minus_fxn(stocks['f124'],40)
        stocks['f140'] = plus_minus_fxn(stocks['f125'],20)
        stocks['f141'] = plus_minus_fxn(stocks['f125'],40)
        stocks['f142'] = plus_minus_fxn(stocks['f126'],20)
        stocks['f143'] = plus_minus_fxn(stocks['f126'],40)
        stocks['f144'] = plus_minus_fxn(stocks['f127'],20)
        stocks['f145'] = plus_minus_fxn(stocks['f127'],40)
        stocks['f146'] = plus_minus_fxn(stocks['f128'],20)
        stocks['f147'] = plus_minus_fxn(stocks['f128'],40)
        stocks['f148'] = plus_minus_fxn(stocks['f129'],20)
        stocks['f149'] = plus_minus_fxn(stocks['f129'],40)

        stocks['f150'] = stocks.close/stocks.close.rolling(window=30, min_periods=30).max() - 1
        stocks['f151'] = stocks.close/stocks.close.rolling(window=60, min_periods=30).max() - 1
        stocks['f152'] = stocks.close/stocks.close.rolling(window=90, min_periods=30).max() - 1
        stocks['f153'] = stocks.vol/stocks.vol.rolling(window=30, min_periods=30).max() - 1
        stocks['f154'] = stocks.vol/stocks.vol.rolling(window=60, min_periods=30).max() - 1
        stocks['f155'] = stocks.vol/stocks.vol.rolling(window=90, min_periods=30).max() - 1
        stocks['f156'] = stocks.close/stocks.close.rolling(window=30, min_periods=30).min() - 1
        stocks['f157'] = stocks.close/stocks.close.rolling(window=60, min_periods=30).min() - 1
        stocks['f158'] = stocks.close/stocks.close.rolling(window=90, min_periods=30).min() - 1
        stocks['f159'] = stocks.vol/stocks.vol.rolling(window=30, min_periods=30).min() - 1
        stocks['f160'] = stocks.vol/stocks.vol.rolling(window=60, min_periods=30).min() - 1
        stocks['f161'] = stocks.vol/stocks.vol.rolling(window=90, min_periods=30).min() - 1


        stocks['date'] = pd.to_datetime(stocks['trade_date'], format='%Y%m%d', errors='ignore')
        stocks['month'] = stocks['date'].dt.month
        stocks['weekday'] = stocks['date'].dt.dayofweek
        stocks = pd.concat([stocks,pd.get_dummies(stocks['month'],prefix='month')],axis=1)
        stocks = pd.concat([stocks,pd.get_dummies(stocks['weekday'],prefix='weekday')],axis=1)
        
        stocks.drop(['month','weekday','date'],axis=1,inplace=True)
        stocks.drop(old_features,axis=1,inplace=True)

        new_stocks = pd.merge(new_stocks,stocks,how='left',on='trade_date')
        new_stocks.replace('', np.nan, inplace=True)
        new_stocks.dropna(inplace=True)
        new_file = '../../input/train_data/' + file
        new_stocks.to_csv(new_file,index=False,encoding='utf_8_sig')
        print('{0} is pretrain successfully!'.format(file))
        exit()
    except Exception as e:
        raise e
        #print(str(e))


    