import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('iris.csv')
kmeans = KMeans(n_clusters=3)

coltypes = df.dtypes
cols = len(coltypes)
numcols = []
for d in range(cols):
  if 'int' in str(coltypes[d]) or 'float' in str(coltypes[d]):
    numcols.append(df.columns[d])

for numcol in numcols :
  X = []
  for k in range(df.shape[0]):
    X.append([k,df.iloc[k][numcol]])
  X = np.array(X)
  print("True position w.r.t. attribute :"+str(numcol))
  plt.scatter(X[:,0],X[:,1], label='True Position')
  plt.show()
  print()

  print("Clustered points w.r.t. attribute :"+str(numcol))
  kmeans.fit(X)
  plt.scatter(X[:,0],X[:,1], c=kmeans.labels_, cmap='rainbow')
  plt.scatter(kmeans.cluster_centers_[:,0] ,kmeans.cluster_centers_[:,1], color='black')
  plt.show()
  print("\n\n\n\n\n")
