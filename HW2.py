
import numpy as np

class matrix3x3:
    def __init__(self,x11,x12,x13,x21,x22,x23,x31,x32,x33):
        self.x11 = x11
        self.x12 = x12
        self.x13 = x13
        self.x21 = x21
        self.x22 = x22
        self.x23 = x23
        self.x31 = x31
        self.x32 = x32
        self.x33 = x33
        
    def add(self, B):
        return matrix3x3(self.x11+B.x11, self.x12+B.x12, self.x13+B.x13,
                         self.x21+B.x21, self.x22+B.x22, self.x23+B.x23,
                         self.x31+B.x31, self.x32+B.x32, self.x33+B.x33)

    def substract(self, B):
        return matrix3x3(self.x11-B.x11, self.x12-B.x12, self.x13-B.x13,
                         self.x21-B.x21, self.x22-B.x22, self.x23-B.x23,
                         self.x31-B.x31, self.x32-B.x32, self.x33-B.x33)
                         
    def multiply(self, other):
        a11 = self.x11*B.x11 + self.x12*B.x21 + self.x13*B.x31
        a12 = self.x11*B.x12 + self.x12*B.x22 + self.x13*B.x32
        a13 = self.x11*B.x13 + self.x12*B.x23 + self.x13*B.x33
        a21 = self.x21*B.x11 + self.x22*B.x21 + self.x23*B.x31
        a22 = self.x21*B.x12 + self.x22*B.x22 + self.x23*B.x32
        a23 = self.x21*B.x13 + self.x22*B.x23 + self.x23*B.x33
        a31 = self.x31*B.x11 + self.x32*B.x21 + self.x33*B.x31
        a32 = self.x31*B.x12 + self.x32*B.x22 + self.x33*B.x32
        a33 = self.x31*B.x13 + self.x32*B.x23 + self.x33*B.x33
        return matrix3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    
    def transpose(self):
        return matrix3x3(self.x11, self.x21, self.x31,
                         self.x12, self.x22, self.x32,
                         self.x13, self.x23, self.x33)
    
    def determinant(self):
        return (self.x11*(self.x22*self.x33-self.x23*self.x32)
               -self.x12*(self.x21*self.x33-self.x23*self.x31)
               +self.x13*(self.x21*self.x32-self.x22*self.x31))
    
    def inverse(self):
        if self.determinant() == 0:
            return "inverse not exist"
        else:
            a11 = (self.x22*self.x33 - self.x32*self.x23)  / self.determinant()
            a12 = -(self.x12*self.x33 - self.x32*self.x13) / self.determinant()
            a13 = (self.x12*self.x23 - self.x22*self.x13)  / self.determinant()
            a21 = -(self.x21*self.x33 - self.x31*self.x23) / self.determinant()
            a22 = (self.x11*self.x33 - self.x31*self.x13)  / self.determinant()
            a23 = -(self.x11*self.x23 - self.x21*self.x13) / self.determinant()
            a31 = (self.x21*self.x32 - self.x31*self.x22)  / self.determinant()
            a32 = -(self.x11*self.x32 - self.x31*self.x12) / self.determinant()
            a33 = (self.x11*self.x22 - self.x21*self.x12)  / self.determinant()
            return matrix3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    
    
A = matrix3x3(1,2,3,4,5,6,7,8,9)
B = matrix3x3(2,-1,0,-1,2,0,0,-1,2)

C = A.add(B)
print(C)

D = A.substract(B)
print(D)

E = A.multiply(B)
print(E)

F = A.transpose()
print(F)

G = A.determinant()
print(G)

H = A.inverse()
print(H)



