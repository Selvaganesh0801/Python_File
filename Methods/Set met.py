# set------var={value}

s={10,20,30,40,50,10,20,30}
print(s)
print(type(s))
# len
a=len(s)
print(a)
print(len(s))
print("-------------")
# add
s={10,20,30,40,50}
s.add(60)
print(s)
print("-------------")
# add multiple value
s={10,20,30,40}
e={50,60}
t=s.update(e)
print(t)
print(s)
s.update("python")
print(s)

# remove
s={10,20,30,40,50,60}
s.remove(50)
# s.remove(500)
print(s)
print("------------------")
s.discard(20)
s.discard(200)
print(s)

s={10,20,30,40,50,60}
a=s.pop()
print(a)
print(s)

s.clear()
print(s)

# copy
s={10,20,30,40,50}
a=s.copy()
print(a)
print(s)
print(a==s)

# add list and set
l=[10,20,30]
s={40,50,60}
s.update(l)
print(s)

# add tuple and set
t=(10,20)
s={30,40}
s.update(t)
print(s)

# sorted()
s={10,20,70,50,40,60}
e=sorted(s)
print(e)

# contain
s={10,20,30,40,50}
print(s.__contains__(20))
print(s.__contains__(200))

# in & not in
print(20 in s)
print(200 in s)
print(20 not in s)
print(200 not in s)

#max---min
print(max(s))
print(min(s))

# union
s={10,20,30}
a={40,50}
t=s.union(a)
print(t)
print(s|a)

# intersection
s={10,20,30,40}
e={30,10,20}
t=s.intersection(e)
print(e)
print(t)
print(s&e)

# difference
s={10,20,40}
e={40,30,60,10}
a=s.difference(e)
print(a)
print(s-e)

# symmetric difference
s={10,20,30,40,50,60}
e={10,30,1,2,3}
a=s.symmetric_difference(e)
print(a)

# looping
s={10,20,30,40,50}
for i in s:
    print(i)

for i,e in enumerate(s):
    print(i,e)