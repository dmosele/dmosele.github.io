# 5.3 Diagonalization

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

To define a matrix, we use np.array and put the matrix within parentheses. The syntax for the matrix is to use square brackets to bookend the matrix, square brackets to bookend each row, and commas to separate individual entries and rows.

A = np.array([[5,8,-4],[8,5,-4],[-4,-4,-1]])
print(A)

## Eigenstuff
To compute eigenvalues and corresponding eigenvectors, we use the LA.eig command. Its output is a vector consisting of the eigenvalues (which we will name w) and a matrix consisting of an eigenvector basis (which we will name P). 

w, P = LA.eig(A)

print(w)

print(P)

We can also compute the determinant using the LA.det command. We see that as we recall, the determinant is the product of the eignevalues.

LA.det(A)

## Diagonalization
We will create a new matrix D which is a diagonal matrix with the eigenvalues of c along the diagonal. We then verify that $PDP^{-1}$ is equal to our original matrix c. 
 - To create a diagonal matrix we use the np.diagflat command.
 - To multiply matrices we can use the @ symbol
 - To compute an inverse we can use the LA.inv command

D = np.diagflat(w)
print(D)

P @ D @ LA.inv(P)

## Problems for you to try
Are the matrices $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \text{ and } \begin{bmatrix} 2 & 4 & 3 \\ -4 & -6 & -3 \\ 3 & 3 & 1 \end{bmatrix}$$ diagonalizable?

B = np.array([[1,2],[3,4]])
C = np.array([[2,4,3],[-4,-6,-3],[3,3,1]])

l, Q = LA.eig(B)

print(l)

print(Q)

m, R = LA.eig(C)

print(m)

print(R)

R @ np.diagflat(m) @  LA.inv(R)

