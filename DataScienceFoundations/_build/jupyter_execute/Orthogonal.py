# 6.2 Orthogonal Sets

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

a = np.array([[1],[2],[3]])
b = np.array([[3],[0],[-1]])
c = np.array([[-1],[5],[-3]])

We append the vectors together using the np.concatenate function.

A = np.concatenate((a,b,c),axis=1)
print(A)

np.around(np.transpose(A) @ A, decimals=10)

