#If statement
# asign
a=30
if (a>25):
    print("True")
print("False")
# compare
a=1234
if a==1234:
    print("True")
print("-------------")
# if else
a=20
if a>15:
     print("True")
else:
     print("False")

# if else if
age=20
weight=30

if age>25:
    if weight>25:
        print("Gooo")
    else:
        print("Wait")
else:
    print("Get Out")

# And
a=20
b=30
if(a>15 and b>25):
    print("True")
else:
    print("False")

# Or
a=25
b=35
if (a>30 or b>30):
    print("True")
else:
    print("False")

# if elif
a=10
b=30
c=20
if (a>b and a>c):
    print("True")
elif (b>a and b>c):
    print("Low")
elif (c>a and c>b):
    print("False")

print("----Looping------")

#Looping:
for x in range(1,10):
    if x==5:
        break
    print(x)
print("----------")
for i in range(1,4):
    for j in range(1,3):
        print(j)
    print(i)
print("-------------")
for i in range(1,4):
    for y in range(1,i):
        print(y)
print("-------------")
for i in range(1,4):
    for j in range(i+1,4):
        print(j)
print("--------------")
for i in range(1,4):
    for j in range(i+1,5):
        print(i)

# a=int(input())
# if(a>18):
#     print("Eligible to Vote")
# else:
#     print("Not Eligible")

#find even or odd
def even(num):
    if num%2==0:
        return'Even'
    else:
        return'Odd'
print(even(10))

# print even numbers----(2,4,6...100)
j=[]
for i in range(1,101,1):
    if i%2==0:
        j.append(i)
print(j)

# sum the odd number-----(1,3,5....100)
sum=0
for i in range(1,100,2):
    sum +=i
print(sum)

# count of even number
sum=0
for i in range(1,100,2):
        sum +=1
print(sum)

# factorial number
def fun(num):
    if num<2:
        return 1
    else:
        return num* fun(num-1)
print(fun(5))

# fibonacci number
def fibo(lim):
    seri=[0,1]
    while seri[-1]+seri[-2]<=lim:
        seri.append(seri[-1]+seri[-2])
    return seri
lim=100
print(fibo(lim))
