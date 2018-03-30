import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

data = pd.read_csv('input_data.csv')

X=data.values

M = np.mean(X.T, axis=1)
#print(M)

C = A - M
#print(C)

V = np.cov(C.T)
#print(V)

values, vectors = np.linalg.eig(V)

print(vectors)
print(values)


P = vectors.T.dot(C.T)
print(P.T)
