# Local var--------method level var
# declare
# inside the method

# access
# inside the method


# local var
# declare

class Employee():
    def emp_id(self):
        empid=123
        print(empid)
    def emp_name(self):
        empname="Selva's"
        print(empname)
e=Employee()
e.emp_id()
e.emp_name()

# Instance variable-------object level var

# delcare
# inside class
# inside constructor---------self.variable=value
# inside method--------------self.var=value

#Outside class---------------object.var=value

# access
# inside class
# inside constructor--------call by self.variable
# inside method------------call by self.var

# outside class------call by object.var
class Employee():
     def __init__(self):
         self.username="kumar@gmail.com"
         self.password="1234567"
     def cts_employee(self):
         self.ctsemployee="ram"
     def hex_employee(self):
         self.hexempname="raj"
e=Employee()
e.address="Chennai"
print("-------------Instance value--------------")
# access
class Employee():
    def __init__(self):
        self.username="Amar@gamil.com"
        self.password="09876543"
    def cts_employee(self):
        self.ctsempname="ramu"
        print(self.ctsempname)
        print(self.username)
        print(self.password)
    def hex_employee(self):
        self.hexempname="raju"
        print(self.hexempname)
e=Employee()
e.address="Chennai"
print(e.address)
e.cts_employee()
e.hex_employee()
print(e.ctsempname)
print(e.hexempname)

e.address="Tambaram"
print(e.address)
e.username="Selvag@gmail.com"
print(e.username)

e1=Employee()
print(e1.username)

# Staic var
# declare
# inside class-------classname.var=value
# inside constructor---classname.var=value
# inside instancemethod-----classname.var-value
# inside classmethod---classname.var=value or cls.var=value
# inside static method---classname.var=value
# outside the class---classname.var.value

# access
# inside class---call by classname.var
# inside constructor---call by classname.var
# inside instancemethod-----call by classname.var
# inside classmethod----classnamr.var

# outside the class----classname.var

# declare
class Employee():
    Employee.a=100

    def __init__(self):
        Employee.b=200
    def instancemethod(self):
        Employee.c=300
    @classmethod
    def classmethod(cls):
        Employee.d=400
    @staticmethod
    def staticmethod():
        Employee.e=500
Employee.g=600
e=Employee()

print("--------------Static variable-----------")
class Employee():
    a=100

    def __init__(self):
        Employee.b=200
        print(Employee.a)
        print(Employee.b)
    def instancemethod(self):
        Employee.c=300
        print(Employee.a)
        print(Employee.c)

    @classmethod
    def classmethod(cls):
        Employee.d=400
        cls.e=500
        print(Employee.a)
        print(Employee.b)
        print(Employee.c)
        print(Employee.d)
        print(Employee.e)
    @staticmethod
    def staticmethod():
        Employee.f=600
        print(Employee.a)
        print(Employee.f)

Employee.g=700
e=Employee()
e.instancemethod()
e.classmethod()
e.staticmethod()
print(Employee.g)
print(Employee.a)

print("------------------------------------------")

class Employee():
    username="Kumar"

    def details(self):
        print(Employee.username)
e=Employee()
e.details()

e.username="Ramkeee"
print(e.username)
