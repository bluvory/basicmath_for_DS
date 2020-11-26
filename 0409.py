print("1+3=", 1+3)  # 1+3=4
print("5/2=", 5/2)  # 5/2=2.5
print("9%5=", 9%5)  # 9%5=4
print("5**2=", 5**2)  #5**2=25


print(type(600))       # int
print(type(3.14))      # float
print(type('test'))   # string


x = 10
print(x)
x = 100  # int
print(x)
y = 3.14  # float
print(x*y)
print(type(x*y))  # float


# List ( indexing : starting at 0 )
a = [1,2,3,4,5]
print(a)       # [1,2,3,4,5]
print(a[0])    # 1
print(a[0:3])  # [1,2,3]
print(a[:3])   # [1,2,3]
print(a[:-2])  # [1,2,3]
print(a[2:4])  # [3,4]
print(len(a))  # 5
a[2] = 5  # [1,2,5,4,5]
print(a)