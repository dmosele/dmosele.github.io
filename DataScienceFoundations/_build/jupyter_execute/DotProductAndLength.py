# 6.1 Dot Product, Length, & Orthogonality

First, we import the numpy package and the linear algebra functions within numpy.

import numpy as np
from numpy import linalg as LA

To define our vectors, we use np arrays.

a = np.array([1,2,3])
b = np.array([2,4,-3])
print(a,b)

## Dot Product
To compute the dot product of the vectors a and b defined above, we use the np.dot command.

np.dot(a,b)

## Length
There are several ways to compute the length (norm) of a vector. We can use 
 - The built in norm function LA.norm
 - The square root of the dot product of a vector with itself
 - The square root of the sum of the squares of the components

LA.norm(a)

np.dot(a,a)**0.5

(1**2+2**2+3**2)**0.5

## Orthogonality
Are the vectors a & b above orthogonal? No, as we have already seen that their dot product is zero.

c = np.array([2,2,-2])

np.dot(a,c)

Since a & c have dot product zero, they are orthogonal.

## Problems for you
1. Compute the length of $\vec{w} = \begin{bmatrix} 2 \\ -6 \\ -9 \end{bmatrix}$
2. If $\vec{v} = \begin{bmatrix} 6 \\ 2 \\ -3 \end{bmatrix}$, compute the distance between $\vec v$ and $\vec w$.
3. Are $\vec{v}$ and $\vec w$ orthogonal?

a-b

a+3

w = np.array([2,-6,-9])

v = np.array([6,2,-3])

LA.norm(v-w)

LA.norm(w-v)

np.dot(v,w)

