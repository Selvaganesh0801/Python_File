# a=143
# print("emp_Id:",a)
# b="SelvaG"
# print("emp_Name:"+b)
# c="sg08012001@gmail.com"
# print("emp_Email:"+c)
# d=9488793821
# print("emp_Phone_No:",d)
# e="30,000"
# print("emp_Salary:",e)
# f=True
# print("emp_Gender:Male",f)
# g="ChennI"
# print("emp_City:"+g)

# print(int(input("StudentId:")))
# print(str(input("StudentName:")))
# a=int(input("Mark_1:"))
# print(a)
# b=int(input("Mark_2:"))
# print(b)
# c=int(input("Mark_3:"))
# print(c)
# d=int(input("Mark_4:"))
# print(d)
# e=int(input("Mark_5:"))
# print(e)
# f=(a+b+c+d+e)
# print("TOTal:",f)
# h=f/5
# print("Average mark:",h)

# a=int(input("student_Id:"))
# print(a)
# b=str(input("student_Name:"))
# print(b)
# c=str(input("student_Email:"))
# print(c)
# d=int(input("student_Phone_NO:"))
# print(d)
# e=str(input("student_Dept:"))
# print(e)
# f=bool(input("student_Gender:"))
# print(f)
# g=str(input("student_City:"))
# print(g)

for x in range(1,10):
    if x==5:
        print(x)
print("_____________________")
for x in range(1,10):
    if x==5:
        break;
    print(x)
print("_____________________")
for x in range(1,10):
    if x==5:
        continue
    print(x)
print("_____________________")
for x in range(1,4):
    for y in range(1,4):
        print(y)
    print(x)
    print("")
print("_____________________")
for x in range(1,4):
    for y in range(1,4):
        print(x)
print("_____________________")
for x in range(1,4):
    for y in range(1,x):
        print(y)
    print(x)
print("_____________________")
for x in range(0,15,2):
    for y in range(0,x+1 ):
        print("*",end="")
    print("")
print("_____________________")
