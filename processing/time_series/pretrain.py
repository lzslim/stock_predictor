import os
import pandas as pd
import numpy as np
import tushare as ts
import re

PERIOD = 5
path = '../../input/daily'
files = [i[2] for i in os.walk(path)][0]
api = ts.pro_api('5eef637df39eb0825334332ed97adca119e221805c63c549836377f7')
pro = ts.pro_api()
count = 0
for i, file in enumerate(files[31:-12]):
    count += 1
    basic_filename = path + '/' + file
    basic_stocks = pd.read_csv(basic_filename,encoding='utf_8_sig')
    drop_list = ['name','pre_close','change','pct_chg',
        'amount','turnover_rate_f','pe_ttm','pb','ps',
        'ps_ttm','total_share','float_share','free_share',
        'total_mv','circ_mv','trade_date_y','trade_date_x','industry']
    extra_list = ['industry','trade_date_x','volume_ratio','pe','target']
    basic_stocks.drop(drop_list,axis=1,inplace=True)
    for j in range(PERIOD):
        filename = path + '/' + files[i-j+4]
        stocks = pd.read_csv(filename,encoding='utf_8_sig')
        drop_list.extend(extra_list)
        stocks.drop(drop_list,axis=1,inplace=True)
        stocks.rename(columns={'open':'open_'+str(j+1),'high':'high_'+str(j+1),
            'low':'low_'+str(j+1),'close':"close_"+str(j+1),
            'vol':'vol_'+str(j+1),'turnover_rate':'turnover_rate_'+str(j+1)},inplace=True)
        basic_stocks = pd.merge(basic_stocks,stocks,how='left',on='ts_code')
    basic_stocks.replace('', np.nan, inplace=True)
    basic_stocks.dropna(inplace=True)
    #加入大盘因素
    trade_date = re.findall(r'\d+',file)[0]
    index = pro.index_daily(ts_code='000001.SH',start_date=trade_date,end_date=trade_date)
    basic_stocks['index_pct_chg'] = index.iloc[0,8]
    index = pro.index_dailybasic(ts_code='000001.SH',start_date=trade_date,end_date=trade_date)
    basic_stocks['index_turnover_rate'] = index.iloc[0,7]
    #把target列调整到最后一列
    target = basic_stocks['target']
    basic_stocks.drop(labels=['target'], axis=1,inplace=True)
    basic_stocks.insert(len(basic_stocks.columns), 'target', target)
    new_path = '../../input/train_data/' + file
    basic_stocks.to_csv(new_path,index=False,encoding='utf_8_sig')
    print('{0} pretrain successfully!'.format(file))
    if count == 18:
        count = 0
        time.sleep(60)