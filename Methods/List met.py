#  0   1 2  3  4  5  6
s=[10,20,30,40,50,60,70]
# -7 -6 -5 -4 -3 -2 -1
print(s)
print(len(s))
# sliceope
print(s[:-7:-1])
print(s[4])

#add values in list on 3types(append,insert,extends)
g=[11,22,33,44,55,66]
#append
g.append([77,88])
print(g)
#insert
g.insert(2,23)
g.insert(5,67)
g.insert(7,100)
print(g)
#extends
g.extend([10,20])
print(g)
g.extend("selvag")
print(g)
#remove the object use(remove,pop,delete)
#remove
g.remove(22)
g.remove("e")
print(g)
#pop
g.pop()
print(g)
#del
del g[3]
print(g)
del g[0:4]
print(g)

#index
sg=[10,11,12,13,14,15,16,11,10]
print(sg.index(11))
print(sg.index(11,3))
print(sg.index(15,4,6))

#count
print(sg.count(15))

#sort
sg.sort()
print(sg)
sg.sort(reverse=True)
print(sg)
s=[10,20,30,50,40]
i=sorted(s)
print(i)
print("-------------")
#to print all values

#looping
#for loop

for i in range(0,len(sg)):
    print(sg[i])
print("----------------")
for i in s:
    print(i)
print("-------------------")
for i ,v in enumerate(s):
    print(i,v)