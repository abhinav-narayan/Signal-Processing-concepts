"""Circular Convolution """
import numpy as np
from scipy.fftpack  import fft,ifft
import matplotlib.pyplot as plt
xn=[1,2,3,4,8]
hn=[5,4,8,2,0]

A=fft(xn)
B=fft(hn)

C=A*B
D=ifft(C)

print(D)

plt.stem(xn)
plt.title('input')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.stem(hn)
plt.title('input 2')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.show()

plt.stem(np.absolute(D))
plt.title('output')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()