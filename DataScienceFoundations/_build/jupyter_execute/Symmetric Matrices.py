# 7.1 Symmetric Matrices

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

To define a matrix, we use np.array and put the matrix within parentheses. The syntax for the matrix is to use square brackets to bookend the matrix, square brackets to bookend each row, and commas to separate individual entries and rows.

A = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
print(A)

## Eigenstuff
To compute eigenvalues and corresponding eigenvectors, we use the LA.eig command. Its output is a vector consisting of the eigenvalues (which we will name w) and a matrix consisting of an eigenvector basis (which we will name P). 

w, P = LA.eig(A)

print(w)

print(np.around(P,3))

Note that this eigenvector basis is orthonormal. (The "normal" part of it is a feature of Python, but it should be orthogonal nonetheless)

np.around(np.transpose(P) @ P)

## Diagonalization
We will create a new matrix D which is a diagonal matrix with the eigenvalues of c along the diagonal. We then verify that $PDP^{-1}$ is equal to our original matrix c. 
 - To create a diagonal matrix we use the np.diagflat command.
 - To multiply matrices we can use the @ symbol
 - To compute an inverse we can use the LA.inv command

D = np.diagflat(w)
print(D)

P @ D @ LA.inv(P)

