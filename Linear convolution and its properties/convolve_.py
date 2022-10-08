"""To convolve two simple sequences """

import numpy as np

import matplotlib.pyplot as plt
a=[5,-10,15,-20]
b=[2,-4,-6,8,10]

c=np.convolve(a,b)


print(c)

#Expected Results
#  10  -40   40    0  -40  140  -10 -200

plt.stem(a)
plt.title('input 1')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

plt.stem(b)
plt.title('input 2')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.show()

plt.stem(c)
plt.title('output')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.show()


