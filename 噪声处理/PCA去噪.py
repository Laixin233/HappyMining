import numpy as np
import matplotlib.pyplot as plt
#-----------------------------------------------------------------
X=np.empty((150,2))
X[:,0]=np.random.uniform(0.,150.,size=150)
X[:,1]=0.8*X[:,0]+5.+np.random.normal(0,5,size=150)
#-----------------------------------------------------------------
from sklearn.decomposition import PCA
def ReadReductionofcomponents(X):
    pca=PCA(n_components=1)
    pca.fit(X)
    x_reduction =pca.transform(X)
    x_restore=pca.inverse_transform(x_reduction)
    plt.scatter(X[:,0],X[:,1])
    plt.scatter(x_restore[:,0],x_restore[:,1])
    plt.show()
#--------------------------------------------
def ReadReductionofRatio(X):
    pca=PCA(0.96)
    pca.fit(X)
    x_reduction=pca.transform(X)
    x_restore=pca.inverse_transform(x_reduction)
    plt.scatter(X[:,0],X[:,1])
    plt.scatter(x_restore[:,0],x_restore[:,1])
    plt.show()
ReadReductionofcomponents(X)
ReadReductionofRatio(X)
