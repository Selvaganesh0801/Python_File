# Instance variable

class Employee():
    country="India" #static var
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def cts_employee(self):
        print("Cts employee")
        print("Cts employee name is",self.name,"Employee id id",self.empid)
        print(Employee.country)
    def hex_employee(self):
        print("Hexaware Employee")
        print("Hex employee is ",self.name,"Employee id is",self.empid)
        print(Employee.country)

e=Employee("Selvag",143)
e.cts_employee()
e.hex_employee()

# calling instance method inside the instance method
print()
class Employee():
    country="India"
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def cts_employee(self):
        print("Cts Employee")
        print("Cts employee name is",self.name,"Employee id is ",self.empid)
        print(Employee.country)
    def hex_employee(self):
        print("Hexaware Employee")
        print("Hex employee name is ",self.name,"Employee id is",self.empid)
        self.cts_employee()

e=Employee("SelvaG",1443)
e.hex_employee()

print("-------------Class Method-----------")
class Employee():
    country="India"
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    @classmethod
    def cts_employee(cls): #cls------indicate class
        print("Cts Employee")
        # print("Cts employee name is",cls.name,"employee id is",cls.empid)
        print(Employee.country)
    @classmethod
    def hex_employee(cls):
        print("Hexaware Employee")
        print(Employee.country)

e=Employee("Ganesh",123)
e.cts_employee()
e.hex_employee()

class Employee():
    country="India"
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    @classmethod
    def cts_employee(cls): #cls------indicate class
        print("Cts Employee")
        # print("Cts employee name is",cls.name,"employee id is",cls.empid)
        print(Employee.country)
    @classmethod
    def hex_employee(cls):
        print("Hexaware Employee")
        print(Employee.country)

e=Employee("Ganesh",123)
e.hex_employee()

# staticmethod

class Employee():
    country="India"
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    @staticmethod
    def cts_employee(id): #argument
        print("Cts employee")
        print(id)
        print(Employee.country)
    @staticmethod
    def hex_employee():
        print("Hexaware employee")
        print(Employee.country)
e=Employee("Selva",143)
e.hex_employee()
e.cts_employee(1443)



class Employee():
    country="India"
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid

    @staticmethod
    def cts_employee(): #argument
        print("Cts employee")
        print(id)
        print(Employee.country)
    @staticmethod
    def hex_employee():
        print("Hexaware employee")
        print(Employee.country)
e=Employee("Selva",143)
e.hex_employee()
Employee.cts_employee()