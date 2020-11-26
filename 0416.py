# function
def factorial(n):
    mult = 1
    for k in range(1, n+1):
        mult = mult*k
    return mult

a = factorial(20)  # a <- 20!
print('20!=', a)
print('20!=', factorial(20))

다름이름으로 저장 functions
(같은폴더에 들어있어야함)

from functions import *
a = factorial(20)
print('20!=', a)


# class

class class_name:
    def __init__(self, input):  # constructor
        something
    def method_1(self, input):  # method 1
        something
    def method_2(self, input):  # method 2
        something

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
print( "Initialized with(" , x , "," , y ,")" )

    def sqrt_magnitude(self):
        return self.x*self.x + self.y*self.y

    def inner_product(self, v1)
        return self.x*v1.x + self.y*v1.y


# Test on Vector2D class
v1 = Vector2D(1, 9)
sqrt_mag_v1 = v1.sqrt_magnitude()
print(sqrt_mag_v1)

v2 = Vector2D(4, 6)
v1_dot_v2 = v2.inner_product(v2)
print(v1_dot_v2)



# Numpy
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])
print(x)
print(type(x))

y = np.array([2.0, 3.0, 5.0, 9.0])
print('x+y=', x+y)
print('x-y=', x-y)
print('x*y=', x*y)  # component-wise
print('x/y=', x/y)  # component-wise


A = np.aray([[1, 2] , [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.aray([[1, 0] , [0, 4]])
print('A+B=', A+B)
print('A-B'=', A-B)
print('A*B=', A*B)  # component-wise
print('A/B=', A/B)  # component-wise
