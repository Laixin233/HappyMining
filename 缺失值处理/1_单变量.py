
from sklearn.impute import SimpleImputer
import numpy as np


def deal_im(X):
    """
    缺失值处理
    单变量插补的处理策略（由strategy参数制定）有四个：mean，median，most_frequent和constant（搭配fill_value参数使用）。
    其中，mean和median分别表示使用均值和中位数来插补缺失值；对于定性数据，可以使用most_frequent（众数）来插补缺失值。
    :return:
    """
    si = SimpleImputer(missing_values=np.nan, strategy='mean')
    X = si.fit_transform(X)


   # 输出填充数据后的数据
    print(X)


if __name__ == "__main__":
    data = [[9, np.nan], [1, 5], [2, 4]]
    deal_im(data)