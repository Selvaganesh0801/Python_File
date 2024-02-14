#dictionary
d={10:'Selva',20:'ganesh',30:'karthi',40:'arun',50:'arnold'}
print(d)
print(type(d))
#lenth
print(len(d))
#sliceoperator
a=d[30]
print(a)

#get
print(d.get(20))
print(d.get(200))

#add
d={10:'Selva',20:'ganesh',30:'karthi',40:'arun',50:'arnold'}
d[60]='kishore'
print(d)
a={70:'muthu',80:'krish'}
d.update(a)
print(a)
print(d)

#replcae
d={10:'Selva',20:'ganesh',30:'karthi',40:'arun',50:'arnold'}
d[40]="atchaya"
print(d)

#remove
#pop
d.pop(40)
print(d)
d.popitem()
print(d)

#max---&----min
d={10:'Selva',20:'ganesh',30:'karthi',40:'arun',50:'arnold'}
print(max(d))
print(min(d))
print("--------------")
#key
k=d.keys()
print(k)

for i in k:
    print(i)

print("-------------")

#values
v=d.values()
print(v)

for  i in v:
    print(i)

print("-------------")
#key and values-----pair-------item
d={10:'Selva',20:'ganesh',30:'karthi',40:'arun',50:'arnold'}
a=d.items()
print(a)
print(type(a))

for i in a:
    print(i)
print()
for i in enumerate(d):
    print(i)
print("--------------")

for i,v in enumerate(a):
    for j in enumerate(v):
     print(j)

