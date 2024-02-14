class Employee():
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
# var=classname()
e=Employee()
e.add()

# constructor declaration
# def __init__():
# to invoke constructor we have to create a object

class Employee():
    def method(self):
        print("Method")
    def __init__(self):
        print("Constructor")
e=Employee()
e.method()

class Employee():
    def __init__(self):
        self.a=10
        self.b=10

    def sum(self):
        c=self.a+self.b
        print(c)
e=Employee()
e.sum()

# Non-Parameterized or Default Constructor

class Employee():
    def __init__(self):
        self.empid=1443
        self.empName='SelvaG'
    def emp_Id(self):
        print("My employee id is",self.empid)

    def emp_Name(self):
        print("My employee name is",self.empName)
e=Employee()
e.emp_Id()
e.emp_Name()

# Parameterized or Argument based Constructor
class Employee():
    def __init__(self,id,name):
        self.empid=id
        self.empName=name

    def emp_Id(self):
        print("My employee id is",self.empid)
    def emp_Name(self):
        print("My employee name is",self.empName)
e=Employee(123,'Selva')
e.emp_Id()
e.emp_Name()

class Employee():
    def __init__(self):
        print("Default")
    def __int__(self,id):
        print("Argument*_*")

g=Employee()
g.__int__(123)


class Employee():

    def m1(self,id):
        print("Argument")
    def m2(self):
        print("Default*_*")
    def __init__(self):
        print("Hello")
e=Employee()
e.m1(143)
e.m2()

