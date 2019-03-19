import tushare as ts
import datetime
import pandas as pd

def filter_ST_stock(pro):
    #查询当前所有正常上市交易的股票列表
    stocks = pro.stock_basic(exchange='', list_status='L', fields='ts_code,name')
    stocks = stocks[stocks.name.str.contains('ST')]
    st_stock_codes = stocks['ts_code'].tolist()
    return st_stock_codes

def getSomeDay(day):
    today = datetime.date.today()
    period = datetime.timedelta(days=day)
    someday = today - period
    return someday

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

def check_target(pct_chg_period,target):
    if target != 1 and pct_chg_period >= 5:
        target = 1
    return target