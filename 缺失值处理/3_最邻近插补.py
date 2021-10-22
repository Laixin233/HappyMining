import numpy as np
from sklearn.impute import KNNImputer

imputer = KNNImputer(n_neighbors=2)
X = [[1, 2, np.nan], [3, 4, 3], [np.nan, 6, 5], [8, 8, 7]]
X= imputer.fit_transform(X)
print(X)