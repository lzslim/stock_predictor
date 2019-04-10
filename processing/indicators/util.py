import pandas as pd
import numpy as np

def tag(x,n):
    data = pd.DataFrame()
    data['pct_chg'] = x
    del(x)
    data['target'] = 0
    for i in range(1, n+1):
        data['pct_chg_sum'] = data.pct_chg.rolling(window=i).sum()
        data['target'] = data.dropna().apply(lambda x: set_taget(x['pct_chg_sum'], x['pct_chg'], x['target']),axis=1)
    return data['target']

def set_taget(pct_chg_sum, pct_chg, target):
    res = 0
    pct_chg_sum = pct_chg_sum - pct_chg
    if target == 1:
        res = 1
    else:
        if pct_chg_sum >= 5 and pct_chg <= 7:
            res = 1
    return res

def pct_chg_fxn(x,n):
    return x.pct_change(n)

def ma(x,n):
    return x.rolling(n).mean()

def ema(x,n):
    return x.ewm(span=n).mean()

def zscore_fun(x,n,m):
    return (x - x.rolling(window=n, min_periods=m).mean())/x.rolling(window=n,min_periods=m).std()

def plus_minus_fxn(x,n):
    return x.rolling(n).sum()

