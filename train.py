import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score,roc_auc_score,accuracy_score
from sklearn.metrics import roc_curve, auc, recall_score, precision_score
import matplotlib.pyplot as plt
import xgboost as xgb
from operator import itemgetter
import datetime

def create_feature_map(features):
    outfile = open('./model/xgb_indicators.fmap', 'w')
    for i, feat in enumerate(features):
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
    outfile.close()

def get_importance(gbm, features):
    create_feature_map(features)
    importance = gbm.get_fscore(fmap='./model/xgb_indicators.fmap')
    importance = sorted(importance.items(), key=itemgetter(1), reverse=True)
    return importance

stocks = pd.read_csv('input/all_data_8_indictors.csv',encoding='utf_8_sig')
stocks.drop(['ts_code'],axis=1,inplace=True)
stocks.drop(['trade_date'],axis=1,inplace=True)

#划分训练集和测试集
X = stocks.drop(['target'],axis=1)
#X = X[['k','d','j']]
features = list(X.columns.values)
y = stocks['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
#X_train = X
#y_train = y

sumw = y_train.value_counts().values
sumwpos = sumw[1]
sumwneg = sumw[0]
print('*' * 30)
print(y_train.value_counts())
print('*' * 30)
print(y_test.value_counts())

#训练
# xgboost
X_dtrain = xgb.DMatrix(X_train, label=y_train)
X_dtest = xgb.DMatrix(X_test, label=y_test)
del(X_train)
del(X_test)
# aucpr
param = {
    'eta':0.1,
    'silent': 1,
    'eval_metric':['aucpr'],
    'booster':"gbtree",
    'scale_pos_weight': 1, 
    'max_depth':4
}
evallist = [(X_dtest, 'eval'),(X_dtrain,'train')]
#evallist = [(X_dtrain,'train')]
num_round = 150
bst = xgb.train(param, X_dtrain, num_round, evallist, early_stopping_rounds=10)

#print('Saving model...')
#model_name = './model/xgb_indicators_{0}.model'.format(datetime.date.today().strftime("%Y%m%d"))
#bst.save_model(model_name)

#bst = xgb.Booster()
#bst.load_model('./model/xgb_indicators_20190325.model')

print('Validating...')
check = bst.predict(X_dtest)

print(check)
print(check.shape)
print('*' * 30)
print(y_test.values)
print(y_test.shape)

score = average_precision_score(y_test.values,check)
print('area under the precision-recall curve: {:.6f}'.format(score))
print('*' * 30)

check2 = check.round()
score = precision_score(y_test.values,check2)
print('precision score: {:.6f}'.format(score))
print('*' * 30)

answer = pd.DataFrame()
answer['predict_prob'] = pd.Series(check).astype('float64')
answer['predict'] = pd.Series(check2).astype('int64')
answer['target'] = pd.Series(y_test.values).astype('int64')
answer.to_csv('input/answer.csv',index=False)

score = recall_score(y_test.values, check2)
print('recall score: {:.6f}'.format(score))
print('*' * 30)

# score = roc_auc_score(y_test.values,check)
# print('area under the roc curve: {:.6f}'.format(score))
# print('*' * 30)

# check2 = check.round()
# score = accuracy_score(y_test.values,check2)
# print('accuracy score: {:.6f}'.format(score))
# print('*' * 30)

imp = get_importance(bst, features)
print('Importance array: ', imp)




