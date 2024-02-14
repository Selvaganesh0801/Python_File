#Tuple

t=(10,20,30,90,10,10,40,50)
print(len(t))
t=("python","selenium","sql","java")
print(len(t))

t=(10,20,30,90,10,10,40,50)
print(t.index(10))
print(t.index(10,5,6))
print(t.index(50))
# print(t.index(200))
print(t.index(10,4,6))

t=(10,20,30,40,50,60)
print(t[2])
print(t[4])
# print(t[12])
print(t[-3])
# print(t[-8])

t=(10,20,30,90,10,10,40,50)
u=(100,20)
l=t+u
print(l)

t=(10,20,30,90,10,10,40,50)
e=("python","java")
p=t+e
print(p)

t=(10,20,30,90,10,10,40,50)
u=(100,200,300)
p=t+u
print(p)
print(type(p))

t=(10,20,30,90,10,10,40,50)
print(t.count(10))

print(max(t))
t=('python','java','sql','selenium')
print(type(t))
print(min(t))
print(max(t))

s=('welcome')
t=('python')
u=s+t
print(u)
print(type(u))

t=(105,205,305,405,505,605,705,805)
print(200 not in t)
print(505 not in t)

t=(10,20,30,40,50,60)
t1=(10,20,30,40,50,60)
u=t==t1
print(u)
u=(10,20,30,40,50,60)
u1=(60,20,30,40,50,10)
p=u==u1
print(p)

t=(105,205,305,405,505,605,705,805)
for i in range(0,len(t)):
    print(t[i])
print("-----------")
for i in t:
    print(i)

t=(105,205,305,405,505,605,705,805)
for i in enumerate(t):
    print(i)

for i,v in enumerate(t):
    print(i,v)