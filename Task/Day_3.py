# List
l=[10,20,30,90,10,10,40,50]
print(len(l))

l=[10,20,30,90,10,50]
print(l.index(10))
print(l.index(10,2,6))
print(l.index(50,0,6))
print(l.index(90,2,4))

l=[10,20,30,90,10,10,40,50,10]
print(l.index(10))

l=[10,20,30,90,10,10,40,50,10]
l.append([100,200,300])
print(l)
print(type(l))
# print(l.index())

l=[10,20,30,90,10,10,40,50,10]
l.extend([100,200,300])
print(l)
print(l.index(200))

l=[10,20,30,90,10,10,40,50,10]
l.remove(10)
print(l)
l.pop()
print(l)
l.remove(40)
print(l)
l.pop(3)
print(l)

l=[10,20,30,90,10,10,40,60,80,100]
del (l[3])
print(l)
del (l[-5:-1])
print(l)
l=[10,20,30,90,10,10,40,60,80,100]
del (l[2:10])
print(l)
l.clear()
print(l)

l=[100,200,300,400,500,600,700]
l.insert(2,350)
print(l)

l=[10,20,30,90,10,10,40,50]
l.append([100,200,300])
print(l)
l=[10,20,30,90,10,10,40,50]
l.extend([100,200,300])
print(l)

l=[10,20,30,90,10,10,40,50]
print(l.count(10))

l=[10,20,30,90,10,10,40,50]
print(max(l))
print((min(l)))

l=[10,20,30,90,10,10,40,50]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

for i in range(0,len(l)):
    print(l[i])

for i,v in enumerate(l):
    print(i,v)

