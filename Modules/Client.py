def fun(a,b):
    print(a+b)
fun(10,20)

z=100
print(z)

# import modulesname calling-----modulesname.var
import Employee
print(Employee.x)
print(Employee.y)

# import modulesname calling modulename.fun
import Employee
Employee.add(10,20)
Employee.sub(20,30)
Employee.mul(11,13)
Employee.div(10,2)
print("-------------")

# import modulename as sg
import Employee as sg
print(sg.x)
print(sg.y)
sg.add(10,20)
sg.sub(50,25)
print("--------------")

def details(a):
    print(a)
details("Helllo")