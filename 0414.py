# { 'dictionary' : value }
city = {'Seoul' : 0, 'Busan' : 1}
print(city['Seoul'])
print(city['Busan'])
city['Bucheon'] = 2
print(city)


# for loop
for k in [1,2,3,4,5]:
    print("Hello Everyone!")
    
    
# Without for loop
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")
print("Hello Everyone!")


# the range function
for k in range(1,6):
    print(k, "squared is", k*k)

for x in range(5, 0, -1):
    print(x)
  

# cumulative loops : summaion
sum = 0
for i in range(1, 21):
    sum = sum + (i*i)
print("sum of first 20 squares is", sum)  #2870


#DIY 20!
fac = 1
for k in range(2,101):
    fac= fac*k
print('100!=', fac)


# while loop
sum = 0
k = 1
while k < 21:
    sum = sum + k*k
    k = k+1
print(sum)


# if / else
score = 50
if score < 60:
    print("Your credit is F")
else:
    print("Your credit is A+")
 
 
# if / elif 효율적


# DIY
import matplotlib.pyplot as plt
a = -2
b = 2
n = 401
dx = (b-a)/(n-1)
x_list = []
y_list = []

for i in range(0,n):
    x = a + i*dx
    y = x**5-5*x**3+4*x
    x_list.append(x)
    y_list.append(y)

plt.plot(x_list, y_list)
plt.show()





