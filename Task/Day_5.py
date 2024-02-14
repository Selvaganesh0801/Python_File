# Set
s={10,20,30,90,10,10,40,50}
print(len(s))
e={'python','selenium','sql','java'}
print(len(e))

s={10,20,30,90,10,10,40,50}
s.add(100)
print(s)

s={10,20,30,90,10,10,40,50}
s.add('python')
print(s)
#
# s={10,20,30,90,10,10,40,50}
# e={100,200,300}
# s.add(e)
# print(s)
#
# s={10,20,30,90,10,10,40,50}
# e={'java','python'}
# s.add(e)
# print(s)

s={10,20,30,90,10,10,40,50}
print(max(s))
print(min(s))
e={'pyhton','java','sql'}
print(max(e))
print(min(e))

s={10,20,30,90,10,10,40,50}
e={100,200,500}
s.update(e)
print(s)

s={100,200,300,400,500,600,700}
e={'java','sql'}
s.update(e)
print(e)

s={10,20,30,90,10,10,40,50}
e={'greens'}
e.update(s)
print(e)

s={10,20,30,90,10,10,40,50}
e={'j'+'greens'}
s.update(e)
print(s)

s={'python'}
print(s)
print(type(s))

l=['java','python',20,30,40]
s={''}
s.update(l)
print(s)
print(type(s))

t=(105,205,305,405,505,605,705,805,'java','python',20,10,60)
s={""}
s.update(t)
print(s)
print(type(s))

s={105,205,305,405,505,605,705,805}
print(200 not in s)
print(505 not in s)

s={10,20,30,40,50,60}
s1={10,20,30,40,50,60}
e=s==s1
print(e)

s={105,205,305,405,505,605,705,805}
for i in s:
     print(i)

for i in enumerate(s):
    print(i)
for i,j in enumerate(s):
    print(i,j)

s={10,20,30,40,50,60}
s1={60,80,90,40,50,10}
e=s.union(s1)
print(e)
print(s|s1)

s={10,20,30,40,50,60}
s1={60,80,90,40,50,10}
e=s.intersection(s1)
print(e)
print(s&s1)

s={10,20,30,40,50,60}
s1={60,80,90,40,50,10}
e=s.difference(s1)
print(e)
print(s-s1)

s={10,20,30,40,50,60}
s1={60,80,90,40,50,10}
e=s.symmetric_difference(s1)
print(e)














































