import tushare as ts
import pandas as pd
from util import *
import time

ts.set_token('5eef637df39eb0825334332ed97adca119e221805c63c549836377f7')
pro = ts.pro_api()

#获取股票列表
basic_stocks = pro.stock_basic(list_status='L',fields='ts_code,name,industry')
basic_stocks = basic_stocks[~basic_stocks.name.str.contains('ST')]
#获取每天的股票信息
start_date = datetime.datetime(2016,3,1)
end_date = datetime.datetime(2019,2,28)
count = 0
while start_date < end_date:
    start_date_str = start_date.strftime("%Y%m%d")
    try:
        stocks = pro.daily(trade_date=start_date_str)
        daily_basic = pro.daily_basic(trade_date=start_date_str)
        if not stocks.empty and not daily_basic.empty:
            stocks = pd.merge(basic_stocks,stocks,how='left',on='ts_code')
            stocks = pd.merge(stocks,daily_basic,how='left',on='ts_code')
            stocks = stocks.dropna()
            path = 'input/daily/daily_stock_' + start_date_str + '.csv'
            stocks.to_csv(path,index=False,encoding='utf_8_sig')
            print('Success {0} stocks!'.format(start_date_str))
    except Exception as e:
        print(e)
        print('*' * 30)

    start_date += datetime.timedelta(days=1)
    count += 1
    if count == 150:
        count = 0
        time.sleep(60)




