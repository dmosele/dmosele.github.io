# 6.3 Orthogonal Projection

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

v1 = np.array([1,-1,1])
v2 = np.array([2,4,2])
y = np.array([3,-1,5])

Find the projection of $y$ onto the subspace $W$ spanned by $v_1$ and $v_2$.

np.dot(y,v1)/np.dot(v1,v1)*v1+np.dot(y,v2)/np.dot(v2,v2)*v2

def ortho_proj(x,u1,u2):
    return np.dot(x,u1)/np.dot(u1,u1)*u1+np.dot(x,u2)/np.dot(u2,u2)*u2

z=y-ortho_proj(y,v1,v2)
print(z)

np.dot(z,v1)

np.dot(z,v2)

LA.norm(z)



