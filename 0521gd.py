import numpy as np
import matplotlib.pyplot as plt

# define function and its derivatives
def f(x,y):
    return np.exp(x+3*y-0.1) + np.exp(x-3*y-0.1) + np.exp(-x-0.1)
  
def fx(x,y):
    return np.exp(x+3*y-0.1) + np.exp(x-3*y-0.1) - np.exp(-x-0.1)
    
def fy(x,y):
    return 3*np.exp(x+3*y-0.1) - 3*np.exp(x-3*y-0.1)
    
# Initialize
x0 = -1.0
y0 = 1.0
a = 0.1
b = 0.7
xk = x0
yk = y0
xlist = []
ylist = []
xlist.append(xk)
ylist.append(yk)
iter = 0

# Gradient Descent method with Backtracking line search
# t = 0.001
while True:
    dx = -fx(xk,yk)
    dy = -fy(xk,yk)
    
    # Backtracking Line Search
    t = 1
    while True:
        fkp1 = f(xk+t*dx, yk+t*dy)
        fk = f(xk, yk)
        if fkp1 < fk - a*t*(dx**2 + dy**2):
            break
        t = b*t
        
    xkp1 = xk + t*dx
    ykp1 = yk + t*dy
    xlist.append(xkp1)
    ylist.append(ykp1)
    
    if np.sqrt((xkp1-xk)**2 + (ykp1-yk)**2) < 10**(-3):
        print("GD converges at iter=", iter)
        break
    
    xk = xkp1
    yk = ykp1
    
    iter += 1
    
# For Visualization
x = np.arange(-4, 3, 0.01)    # -4에서 3까지 0.01간격
y = np.arange(-4, 3, 0.01)

X, Y = np.meshgrid(x, y)    # 정방행렬로 만들기 (좌표축 말하는듯)
Z = f(X, Y)
mask = Z > 20    # Z가 20이상이면 (true로 세팅)
Z[mask] = 0      # 0으로 만든다 즉 20이하일때만 그리기 (20은 그냥 임의의 수)

plt.contour(X, Y, Z)    # 등고선 그리기
plt.plot(xlist, ylist, '-o')
plt.show()

