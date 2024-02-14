print("SelvaG")

#funtions ----- grp of statements
#def funname()

def empid():
    print("Haii Everyone")

# function calling
# funname()

empid()

# function without argument---{-}
def add():
    a=10
    b=20
    c=a+b
    print(c)

add()

# function with arguments

def add(a,b):
    c=a+b
    print(c)

add(10,20)
add("selva","g")

# functions with return arguments

def add(a,b):
    c=a+b
    print(c)
    return c

tot=add(20,30)
tot=add(30,40)
print(tot)

# function with multiple return values

def add(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
tot=add(10,20)
print(tot)
print(type(tot))

# function variable length with key argument

def add(*a):
    print(a)
    return a
c=add(10,11,22,33,44,55)
print(c)

print('--------SelvaG-----------')
def empid(id):
    print(id)
empid(20)

def empname(name):
    print(name)
empname("SelvaG")

# function with key arg
def empdetails(id,name):
    print("Emp_Id",id,"Emp_name",name)
empdetails(143,"selvag")
empdetails("SelvaG",143)

empdetails(id=143,name="selvaG")

# functions with default arg
def empdetails(id=123,name="SG"):
    print("Emp_id",id,"Emp_name",name)
empdetails(id=444)
empdetails(name="Selva")
empdetails(id=23,name="Ganesh")
empdetails()

# function variable length with key arg:
def empdetails(**n):
    print(n)
    print(type(n))
    for i in n.items():
        print(i)
empdetails(name="Selvag",id=1234)
empdetails(name="Selva")
empdetails(id=143)
empdetails(name="Ganesh")
empdetails(age=143)

age=23
name="SelvaG"

print("Employe age is",age,"Employe name is",name)
print("Employe age is {}" "Employe name is {}".format(age,name))
print("Employe age is {}" "Employe name is {}".format(name,age))
print(f"Employe age is {age} Employe name is {name}")
print("Employe age is %d Employe name is %s"%(age,name))
# print("Employe age is %d Employe name is %s"%(name,age))

# Recursive Function
# def fun():
# print("")
# fun ()

# Type of variable
# 1.Local var
# 2.Global var

#Local var---inside the fun,we can accept only with in the funtions

def add():
    a=10
    print(a)
add()

a=10

def add():
    b=20
    c=a+b
    print(c)

def sum():
    print(a)

add()
sum()
print("-------------")
a=10

def fun():
    global c
    a=20
    print(a)
    print(globals()['a'])
    print(globals().get('a'))
    c=15
    print(c)

def sum():
    print(a)
    print(c)

fun()
sum()

count=0
def fun():
    global count
    print('SelvaG',count)
    count=count+2
    if count<=10:
        fun()
fun()

def add(a,b):
    print(a,b)

add(10,20)

def squrt(a):
     return a*a
print(squrt(4))
print(squrt(5))
print(squrt(9))

a=lambda b,c:b+c
print(a(10,20))

e=lambda a:a%2==0

print(e(10))
print(e(15))

print("---------")
# filter
# two arg filter(fun,seq)
# output may be equal or lesser than input
# filter only take true value

l=[1,2,3,4,5,6,7,8]
g=[]
for i in l:
     if i%2==0:
        print(i)
        g.append(i)
print(g)

def isEven(a):
    if a%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8]
g=[]
for i in l:
    if i%2!=0:
        print(i)
        g.append(i)
print(g)

fn=filter(isEven,l)
# list------<
print(list(fn))
print(list(filter(isEven,l)))
# lambda--------<
print(list(filter(lambda a:a%2==0,l)))

 # map
# two arg map(fun,seq)
# output size same as input value
# to do the action based on required

l=[1,3,5,7,9]
g=[]
for i in l:
    c=i*i
    g.append(c)

def squrtit(a):
    return a*a

l=[1,3,5,6,7,9]
g=[]
for i in l:
    c=squrtit(i)
    g.append(c)
print(g)

print(list(map(squrtit,l)))
print(list(map(lambda a:a*a,l)))
# reduce
# input values can be any size but the output will be one
# to do any action based on requirement

l=[1,2,3,4,5,6,7,8]
v=0
for i in l:
    v=v+i
print(v)
# fun
def fun(a,b):
    return a+b
l=[1,2,3,4,5,6,7,8]
v=0
for i in l:
    v= fun(v,i)
print(v)

# form functools import reduce
# print(reduce(fun,l))
# print(reduce(lambda a,b:a+b,l))

print("-------------------")

l=[1,2,3,]
s={4,5,6}
t=(7,8,9)

print(type(l))
print(type(s))
print(type(t))
# list to set
a=list(s)
b=list(t)
c=a+b
print(type(c))
# set
a=set(l)
b=set(t)
print(type(a))
print(type(b))
# tuple
a=tuple(l)
b=tuple(s)
c=a+b
print(type(c))

l=[["selva",1234,"sg2001@gmail.com"],["sel",123,"g2001@gmail.com"],["selvag",143,"gs2001@gmail.com"]]
print(l[0])
print(l[2])
print(l[1][2])

for i in l:
    for j in i:
        print(j)
    print()

d={"name":"selva","id":1234,"mail":"sg2001@gmail.com"}
print(d["id"])

# list to dict

l=[{"name":"selva","id":1234,"mail":"sg2001@gmail.com"},
   {"name":"selv","id":123,"mail":"sg@gmail.com"},
   {"name":"sel","id":12,"mail":"g2001@gmail.com"}]

print(l[0])
print(l[0]["name"])
print(l[0]["id"])
print(l[0]["mail"])

for i in l:
    for j in i.items():
        print(j)
    print()

l=[1,2,3,4,5,6,7,8,9,10]
s=[]
# filter
def even(a):
    # return a%2==0
    if a%3 == 0:
        s.append(a)
f=list(filter(even,l))
print(s)
print(list(filter(lambda a:a%2==0,l)))

# map
m=[10,20,30,40,50]
def add(a):
    return a+5
ad=list(map(add,m))
print(ad)
print(list(map(lambda a:a+5,m)))
# reduce

from functools import reduce
print(reduce(lambda a,b:b/a,m))