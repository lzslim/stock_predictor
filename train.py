import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score,roc_auc_score
from sklearn.metrics import roc_curve, auc, recall_score, precision_score
import matplotlib.pyplot as plt
import xgboost as xgb
from operator import itemgetter

def create_feature_map(features):
    outfile = open('xgb.fmap', 'w')
    for i, feat in enumerate(features):
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
    outfile.close()

def get_importance(gbm, features):
    create_feature_map(features)
    importance = gbm.get_fscore(fmap='xgb.fmap')
    importance = sorted(importance.items(), key=itemgetter(1), reverse=True)
    return importance

stocks = pd.read_csv('input/all_data.csv',encoding='utf_8_sig')
#stocks.drop(['ts_code'],axis=1,inplace=True)
stocks.drop(['trade_date'],axis=1,inplace=True)

#划分训练集和测试集
X = stocks.drop(['target'],axis=1)
features = list(X.columns.values)
y = stocks['target']
del(stocks)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

sumw = y_train.value_counts().values
sumwpos = sumw[1]
sumwneg = sumw[0]
# print(y_test.value_counts())

#训练
# xgboost
X_dtrain = xgb.DMatrix(X_train, label=y_train)
X_dtest = xgb.DMatrix(X_test, label=y_test)
del(X_train)
del(X_test)
param = {
    'eta':0.1,
    'silent': 1,
    'eval_metric':['aucpr'],
    'booster':"gbtree",
    'scale_pos_weight': sumwneg/sumwneg, 
    'max_depth':10
}
evallist = [(X_dtest, 'eval'),(X_dtrain,'train')]
num_round = 50
bst = xgb.train(param, X_dtrain, num_round, evallist, early_stopping_rounds=10)

print('Validating...')
check = bst.predict(X_dtest,ntree_limit=bst.best_iteration+1)

# print(check)
# print(check.shape)
# print('*' * 30)
# print(y_test.values)
# print(y_test.shape)

score = average_precision_score(y_test.values,check)
print('area under the precision-recall curve: {:.6f}'.format(score))
print('*' * 30)

check2 = check.round()
score = precision_score(y_test.values,check2)
print('precision score: {:.6f}'.format(score))
print('*' * 30)

score = recall_score(y_test.values, check2)
print('recall score: {:.6f}'.format(score))
print('*' * 30)

imp = get_importance(bst, features)
print('Importance array: ', imp)




