# 6.5/6.6 Least-Squares

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

Define $A$ and $\vec b$ for the equation $A\vec x=\vec b$ that you would like to solve.

A = np.array([[1,2],[-1,4],[1,2]])
b = np.array([[3],[-1],[5]])
print(A)
print(b)

Check to see if $A^T A$ is invertible.

LA.det(np.transpose(A) @ A)

If it is invertible, we can compute this easily using the inverse of $A^TA$

LA.inv(np.transpose(A) @ A)@np.transpose(A) @ b

np.transpose(A) @ b

