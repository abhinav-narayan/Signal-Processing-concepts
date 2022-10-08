# -*- coding: utf-8 -*-
"""Verification of properties of convolution """
import numpy as np
import matplotlib.pyplot as plt

a=[-1,0,1,2,3]
b1=[5,4,3,2,1]
b2=[6,7,8,9,-1]

c=np.convolve(a,b1) # Commutative property of convolution
d=np.convolve(b1,a)

e=np.convolve(b1,b2)
F=np.convolve(a,e)

g=np.convolve(c,b2)

j= c + np.convolve(a,b2)
k=b1+b2
K= np.convolve(a,k)

print(c)
#[-5 -4  2 12 25 20 14  8  3]

print(d)
#[-5 -4  2 12 25 20 14  8  3]

plt.stem(a)
plt.title('input 1')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.stem(b1)
plt.title('input 2')
plt.xlabel('n')
plt.ylabel('h1(n)')
plt.show()

plt.stem(b2)
plt.title('input 3')
plt.xlabel('n')
plt.ylabel('h2(n)')
plt.show()


plt.stem(c)
plt.title('Commutative property part 1')
plt.xlabel('n')
plt.ylabel('Y(n)')
plt.show()

plt.stem(d)
plt.title('commutative property part 2')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

plt.stem(F)
plt.title('Associative property part 1')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.show()

plt.stem(g)
plt.title('Associative property part 2')
plt.xlabel('n')
plt.ylabel('g(n)')
plt.show()


print(F)
#[-30 -59 -56   9 219 413 530 519 341 191  82  19  -3]

print(g)

#[-30 -59 -56   9 219 413 530 519 341 191  82  19  -3]

#print(j)
#
#
#print(K)

plt.stem(j)
plt.title('3 property of conv')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()

plt.stem(K)
plt.title('3 property of conv')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()