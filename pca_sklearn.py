import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import csv

with open('shuffled_testing.csv',"r") as fin:
    with open('shuffled_testing_input.csv',"w") as fout:
        writer=csv.writer(fout)
        for row in csv.reader(fin):
            writer.writerow(row[:-1])

data = pd.read_csv('shuffled_testing_input.csv')

X=data.values

X = scale(X)

pca = PCA(n_components=3)

pca.fit(X)

var= pca.explained_variance_ratio_
var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print var1

Y=pca.fit_transform(X)

np.savetxt('shuffled_testing_input_pca.csv',Y,delimiter=",")







