# Aritmetic Operator
# +,-,*,/----divide return float,//---floar division,**

# int
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)#----square

print()

# float
a=10.20
b=20.30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)#----square

print()

#complex
a=2+3j
b=3+3j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# print(a//b)----can't use
print(a**b)#----square

print()

# Bool
a=False
b=True
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)#----square

print()

# Str
a="sg"
b="gs"
print(a+b)
print(a*2)
print(b*2)
# print(a*b)

# Relational operators
# <,<=,>,>=,
print()

# int
a=10
b=20
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

print()

# float
a=10.03
b=20.40
print(a<b)
print(a<=b)
print(a>b)
print(a>=b)

print()

# Equality operator
# ==
# !=
print(10==10)
print(10==20)
print(10=="20")
print("10"==20)
print(True==True)
print(False==False)
print(False=="False")

# Logical operator
# and or not

# and---zero true
# zero or empty string--false
# print(x and y) x true return y------x false y return x
print(10 and 20)
print(0 and 20)
print(10 and "ab")

# Or
# non--zero---true
# print(x and y) x true return x-----x false return y
print(10 or 20)
print(0 or 20)
print(10 or "20")
print("" or "20")

# Not
# not------zero false
# zero or empty string True
# not x

print(not 10)
print(not 0)
print(not True)
print(not False)

# Assign operator
# =

print()
a=10
print(a)
a=a+1
print(a)
a+=1
print(a)
a*=2
print(a)
a/=2
print(a)
print()
a=10
print(++a)
print(+(+a))
print(+(-a))
print(-(-a))

# Ternary operator
# python var=statement1 condition else statement2
v="sg" if(10>20) else "gs"
print(v)

# special operators
# membership operator------in not in
print()
l=[10,20,30,40,50]
print(10 in l)
print(100 in l)

s="selvag"
print("s" in s)
print("S" in s)

print("S" not in s )
print("s" not in s )

# identify operator checks the memory of the variable or reference
a=10
b=10
c=30

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)

print( a is not b)
print( a is not c)


# relational chain
print(10<20<30<40<50)
print(10>20>30>40>50)
print("a"<"b"<"c")