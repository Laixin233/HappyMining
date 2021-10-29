import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
#载入数据
dataset=pd.read_csv()
#查看缺失列
print(dataset.info())
#构造缺失集和训练集,以下B是缺失列，A是因变量列
X=pd.DataFrame(dataset)
X_pred=X.dropna(axis=0,subset=['A'])
dataset_pred=dataset[np.isnan(dataset['B'])]
dataset_train=dataset.dropna(subset=['B'],axis=0)
y_pred=np.array(X_pred['B'].T).reshape(-1,1)
X_train=np.array(dataset_train['A'].T).reshape(-1,1)
y_train=np.array(dataset_train['B'].T).reshape(-1,1)
#建模预测
line_reg=LinearRegression()
line_reg.fit(X_train,y_train)
#填充与合并
y_pred=line_reg.predict(np.array(dataset_pred['A']).reshape(-1,1))
dataset_pred=pd.DataFrame(dataset_pred)
dataset_pred.loc[:,'B']=y_pred
dataset_new=dataset_train.append(dataset_pred).sort_values(by='A',axis=0,ascending=True)
print(dataset_new)
