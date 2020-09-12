# 6.4 Gram-Schmidt

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

Merge your basis vectors $\vec x_1,\ldots,\vec x_p$ into a matrix $X$.

X = np.array([[-1.,1,1],[0,1,-1],[1,0,1]])
print(X)

Apply the Gram-Schmidt process to your vectors and output in a new matrix U.

def gramschmidt(V):    
    U = V.copy()
    for x in range (1,np.size(V,1)):
        for y in range (0,x):
            U[:,x] = U[:,x]-(np.dot(V[:,x],U[:,y])/np.dot(U[:,y],U[:,y]))*U[:,y]

    return U    
     

A = gramschmidt(X)

np.around(np.transpose(gramschmidt(X)) @ gramschmidt(X),2)

print(A)

