#String----collection of characters and words
#length
#var=len(storedvar)
s="welcome"
a=len(s)
print(a)
print(len(s))
print("--------------")

#sliceoperator
#var=s[]
a=s[2]
print(a)
print(s[-2])
print(s[-7])
print("----------------")

#storedvalue[start:end:inc]
print(s[0:5:2])
print(s[0:5])
print(s[0:5:2])
print(s[0:7])
print(s[:-8:-1])
print(s[2::1])
print(s[::1])
print("--------------")

#index
print(s.index('c'))
print(s.index('w'))
print(s.index('o'))
print("--------------")

#find
print(s.find('w'))
print(s.find('o'))
print(s.find('m'))
print("--------------")

#starting
#startwith
g="Welcome to python"
print(g.startswith("Wel"))
print(g.startswith("wel"))
print(g.startswith(" Wel"))
print("--------------")

#endwith
print(g.endswith("python"))
print(g.endswith("thon"))
print(g.endswith("on"))
print(g.endswith("on "))
print("--------------")

#--contains---
print(g.__contains__("on"))
print(g.__contains__("emoc"))
print(g.__contains__("e"))
print(g.__contains__("to"))
print(g.__contains__("str"))
print("--------------")

#in
print("come" in g)
print("thon" in g)
print("py" in g)
print("z" in g)
print("--------------")

#notin
print("come" not in g)
print("h"not in g)
print("py"not in g)
print("z"not in g)
print("--------------")

#strip-----unwanted space
h="    Hai SELVAG   "
print(h.strip())

#rstrip
print(h.rstrip())

#lstrip
print(h.lstrip())

#islower
print(h.lower())
print(h.islower())
#upper
print(h.isupper())
print(h.upper())
#capitaliz
i="selva ganesh"
print(i.capitalize())
#title
print(i.title())

print("--------------")

s1="12345"
s2="sgss"
s3="1234sgss"
#isnumeric
print(s1.isnumeric())
print(s2.isnumeric())
print(s3.isnumeric())
print("--------------")
#isalpha
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print("--------------")
#isalnum
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print("----------------")

#split
#var=storedvar.split()
j="Welcome to python"
k=j.split("o")
print(k)
print(len(k))
print(type(k))
print(k[2])
print("--------------")

#var in range(start,len(storedval))
#statement(stordeval[var])
for i in range(0,len(k)):
    print(k[i])


