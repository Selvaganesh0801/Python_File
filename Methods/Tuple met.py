t=(10,20,30,40,50,"py",True,2+3j)
print(t)
print(type(t))
# len
print(len(t))
print("-------------")
# slice
i=t[2]
print(i)
print(t[5])
print(t[6])
# storedvar
print(t[:-9:-1])
# add
t=(10,20,30,40,50)
s=(60,70)
t+=s
print(t)

#count
t=(10,20,30,40,50,60,10,30)
print(t.count(10))
print(t.count(100))

#index
print(t.index(20))
print(t.index(30,1,6))

#contain
print(t.__contains__(50))
print(t.__contains__(90))

#in
print(10 in t)
print(90 in t)

#not in
print(10 not in t)
print(90 not in t)

#maxx,min
print(max(t))
print(min(t))

t=(10,20,30,10,40,50,30)
# sorted
a=sorted(t)
print(a)

t=(10,20,30,40,50,60,10,20,30)

for i in range(0,len(t)):
    print(t[i])
print("---------------")
for i in t:
    print(i)

print("---------------")
for i,j in enumerate (t):
    print(i,"---",j)