__author__ = 'hwang'

import pandas as pd
import numpy as np
from cvxopt import matrix, solvers
import matplotlib.pyplot as plt
from pandas import Series

# Read return data from Excel
data = pd.read_excel('data.xlsx', 'Sheet1', index='Date')
data = data.drop('Date', 1)

meanRets_ls=[] # mean return values
for tic in data.columns.values:
    meanRets_ls.append(data[tic].mean())


# Varianca Covariance Matrix
CVC =data.cov()
CORR = data.corr() # Correlation matrix

# Prepare CVXOPT optimization
np_cvc = np.matrix(CVC)
Q = matrix(np_cvc)
print(Q)

p = matrix(np.zeros(10), (10,1))
print(p)

IDE = np.eye(10)
G = matrix(IDE)
print(G)

h = matrix(np.ones(10))
print(h)

meanRets_arr = np.array( [meanRets_ls])

temp =np.array( [np.ones(10)] )

A = np.concatenate( (temp, meanRets_arr), axis=0)
A = matrix(A)

print(A)
b = matrix([ 1.0, 0 ]) # 2nd row value is expecting return of portfolio
print(b)

# Efficient Frontier
idex = [data.columns.values]
weight_df = pd.DataFrame(index=idex)
stds=[]
finalMean=[]

targetRet = [0, 0.0035 ,0.007, 0.0105, 0.014, 0.0175, 0.021, 0.0245, 0.028, 0.0315, 0.035]

for tr in targetRet:
    b = matrix( [1.0, tr])
    sol = solvers.qp(Q, p, G, h, A, b)
    solv = sol['x']
    weight_df[str(tr)] = Series(sol['x'], index=data.columns.values)
    stds.append(np.ndarray.tolist(np.dot(np.dot(solv.T,CVC),solv)))
    finalMean.append(np.ndarray.tolist(np.dot(solv.T,meanRets_ls)))

stds = np.sqrt(stds)
stds = [stds[i][0][0] for i in range(10)]
finalMean = [ finalMean[i][0] for i in range(10) ]
plt.figtext(0.15,0.6,"Efficient Frontier")
plt.xlabel("Standard Deviation")
plt.ylabel("Returns")
plt.plot(stds,finalMean)
plt.show()