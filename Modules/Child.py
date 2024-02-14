# import modulename1,modulename2
import Employee,Client
print(Employee.x)
print(Employee.y)
print(Client.z)
print("-----------")

# import modulename1 as m1,modulesname2 as m2
import Employee as m1,Client as m2
print(m1.x)
print(m2.z)
m1.add(10,20)
m2.details("Ganesh")
print("--------------")

# from modulename import var
from Employee import x,y
import Employee
print(x)
print(y)
Employee.add(40,50)
print("----------------")

# from modulename import fun
from Employee import add,sub
import Employee
add(10,20)
sub(145,2)
Employee.mul(10,10)
Employee.div(13,11)
print("------------------")

# from modulename import *
from Employee import *
print(x)
add(2,4)
sub(10,3)
mul(11,13)

print("-------------- ")
# different package
# from packagename import modulename
from Login.org import Demo
Demo.fun()
print(Demo.x)

from Login.org.Demo import fun
fun("s","e","l","v","a")