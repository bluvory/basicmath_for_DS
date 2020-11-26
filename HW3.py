import numpy as np
import matplotlib.pyplot as plt

def g(w1, w2):
    return w1**2 + w2**2 + 2*np.sin(1.5*(w1+w2))**2 + 2
  
def gw1(w1, w2):
    return 2*w1 + 6*np.sin(1.5*(w1+w2))*np.cos(1.5*(w1+w2))
    
def gw2(w1, w2):
    return 2*w2 + 6*np.sin(1.5*(w1+w2))*np.cos(1.5*(w1+w2))
    

# stepsize t=10**-2, 10**-1, 10**0 ----------------
w1 = 3
w2 = 3
w1k = w1
w2k = w2
w1list = []
w2list = []
w1list.append(w1k)
w2list.append(w2k)
iter = 0
t = 0.01

while True:
    dw1 = -gw1(w1k, w2k)
    dw2 = -gw2(w1k, w2k)
        
    w1kp1 = w1k + t*dw1
    w2kp1 = w2k + t*dw2
    w1list.append(w1kp1)
    w2list.append(w2kp1)
    
    if np.sqrt((w1kp1-w1k)**2 + (w2kp1-w2k)**2) < 10**(-3):
        print("GD converges at iter =", iter)
        break
    
    if iter > 10000:
        print("GD doesnt't converges!")
        break
    
    w1k = w1kp1
    w2k = w2kp1
    
    iter += 1

    
# Backtracking -------------------------------
w1 = 3
w2 = 3
a = 0.1
b = 0.7
w1k = w1
w2k = w2
w1list = []
w2list = []
w1list.append(w1k)
w2list.append(w2k)
iter = 0

while True:
    dw1 = -gw1(w1k, w2k)
    dw2 = -gw2(w1k, w2k)
    
    t = 1
    while True:
        gkp1 = g(w1k+t*dw1, w2k+t*dw2)
        gk = g(w1k, w2k)
        if gkp1 < gk - a*t*(dw1**2 + dw2**2):
            break
        t = b*t
        
    w1kp1 = w1k + t*dw1
    w2kp1 = w2k + t*dw2
    w1list.append(w1kp1)
    w2list.append(w2kp1)
    
    if np.sqrt((w1kp1-w1k)**2 + (w2kp1-w2k)**2) < 10**(-3):
        print("GD converges at iter by backtracking =", iter)
        break
    
    if iter > 10000:
        print("GD doesnt't converges!")
        break
    
    w1k = w1kp1
    w2k = w2kp1
    
    iter += 1
