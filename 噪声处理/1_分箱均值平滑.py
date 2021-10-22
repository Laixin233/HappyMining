#平滑噪声—等深分箱—均值平滑
import pandas as pd
import numpy as np
def aequilatus_box_mean(data,bins):
    length=data.shape[0]
    labels=[]
    for i in range(bins):
        labels.append('a'+str(i+1))#添加标签
    new_data=pd.qcut(data.iloc[:,0],bins,labels=labels)#等深分箱
    data['label']=new_data
    for label in labels:
        label_index_min=data[data.label==label].index.min()#分箱后索引最小值
        label_index_max=data[data.label==label].index.max()#分箱后索引最大值
        data.loc[label_index_min:label_index_max,data.columns[0]]=np.mean(
            data.A[label_index_min:label_index_max+1,])#根据label及索引，修改A为各箱均值
    return data

if __name__=="__main__":
    data=pd.DataFrame({'A':[11,13,15,20,20,23,26,29,35]})
    bins=3
    print("均值平滑")
    print(aequilatus_box_mean(data,3))
