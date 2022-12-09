# -*- coding: utf-8 -*-
import numpy as np

"""
N point DFT function

"""
inp_sig = [1,1,1,1,0,0,0,0]

N = len(inp_sig)

#print(N)
X = []
#Compute DFT 
for k in range(0,N):
    Xk = 0
    for n in range(0,N):
        Xk += inp_sig[n] * np.exp((-1.0j*2*np.pi*k*n)/N)
    print(Xk)
