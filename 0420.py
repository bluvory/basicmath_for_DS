import numpy as np

# numpy array
A = np.array([[1,2], [3,4]])
print(A[0])  # [1, 2]
print(A[0][1])  # 2
print((A[0])[1])  # 2

A = A.flatten()
print(A)  # [1,2,3,4]
print(A>3)  # [f,f,f,t]
print(A[A>3])  # 4
print(A[A>1])  # [2,3,4]


# matrix-matrix multiplication : np.dot (내적)
A = np.array([[1,2], [3,4]])
B = np.array([[3,4], [5,6]])
AB = np.dot(A, B)
print('AB=', AB)  # [[13,16], [29,36]]


# transpose of matrix : T
A = np.array([[1,2], [3,4]])
AT = A.T
print('AT=', AT)  # [[1,3], [2,4]]


# determinant : np.linalg.det
# import np.linalg as LA

A = np.array([[1,2], [3,4]])
print(np.linalg.det(A))  # -2
B = np.array([[2,1,-1,3], [-2,1,3,1], [0,5,1,4], [4,2,-3,5]])
print(np.linalg.det(B))  # -8


# inverse : np.linalg.inv
A = np.array([[1,2], [3,4]])
Ainv = np.linalg.inv(A)
print(Ainv)


# eigenvalue, eigenvector : np.linalg.eig
A = np.array([[2,-1], [-1, 2]])
eig_vals, eig_vecs = np.linalg.eig(A)
print(eig_vals)
print(eig_vecs)



