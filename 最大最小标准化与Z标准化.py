from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import pandas as pd
X=pd.read_csv(r"C:\Users\87571\Desktop\欧阳的大宝贝（以及一些垃圾）\DD.csv",encoding='utf-8')
Xnew=MinMaxScaler().fit_transform(X)
print(Xnew)
Xnew2=StandardScaler().fit_transform(X)
print(Xnew2)