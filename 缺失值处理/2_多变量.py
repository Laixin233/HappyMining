
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np


imp = IterativeImputer(max_iter=10, random_state=0)
X = [[9, np.nan], [1, 5], [2, 4]]
print(imp.fit_transform(X))

