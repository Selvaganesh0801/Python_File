#Looping Statement
#For,Nested For,While
#one action run in again again is called looping---------<
#for variablename in range(start,end,inc/dec)
#statement("")

#for loop
for a in range(0,5,1):
    print(a)

print("------------------------")
#Nested for loop

for a in range(0,2,1):
    for b in range(0,3,1):
        print(b)
    print(a)

print("--------------------")
#while loop

a=10
while(a<21):
    print(a)
    a=a+2

print("-------------------")

#keywords break,continue,exit(0,-1)-------<
print("-----ON---------")
print("-----OFF--------")
for s in range(0,10,1):
    if s==5:
       exit("SELVAG")
    print(s)
print("-----Stop------")


