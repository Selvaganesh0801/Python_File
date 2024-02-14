class Employee():
    def emp_id(self):
        print("Employee id is 143")
    def emp_name(self):
        print("Employee name is SG")
e=Employee()
e.emp_id()
e.emp_name()
print('-------------------------------')
# Single inheritance

class Company(Employee):
    def company_id(self):
        print("Company id is 1443")
    def compant_name(self):
        print("Company name is React")
f=Company()
f.company_id()
f.compant_name()
e.emp_id()
e.emp_name()
print('--------------------------------')

# Multilevel inheritance---------one child two parent(Grand parent,Parent)

class Client(Company):
    def client_id(self):
        print("Client id is 123")
    def client_name(self):
        print("Client name is Sura")
g=Client()
g.client_id()
g.client_name()
g.company_id()
g.compant_name()
g.emp_id()
g.emp_name()
print("----------------------------------------")

# Multiple inheritance-----two parent one child
class Employee():
    def emp_id(self):
        print("Employee is id 143")
    def emp_name(self):
        print("Employee name is SG ")

class Company():
    def cmp_id(self):
        print("Company id is 1443")
    def cmp_name(self):
        print("Company name is React")

class Client(Employee,Company):
    def client_id(self):
        print("Client id is 123")
    def client_name(self):
        print("Client name is Sura")

g=Client()
g.client_id()
g.client_name()
g.emp_id()
g.emp_name()
g.cmp_id()
g.cmp_name()
print("--------------------------------------")

# Hierarechical Inheritance-----one parent multiple child
class Employee():
    def emp_id(self):
        print("Employee id is 143")
    def emp_name(self):
        print("Employee name is SG")

class Company(Employee):
    def cmp_id(self):
        print("Company id is 1443")
    def cmp_name(self):
        print("Company name is React")
f=Company()
f.cmp_id()
f.cmp_name()
f.emp_id()
f.emp_name()

class Client(Employee):
    def client_id(self):
        print("Client id is 123")
    def client_name(self):
        print("Client name is Sura")
g=Client()
g.client_id()
g.client_name()
g.emp_id()
g.emp_name()
print("----------------------------------")

# Hybrid inheritance----------------combination any two or more type of inheritance
class Employee():
    def emp_id(self):
        print("Employee id is 143")
    def emp_name(self):
        print("Employee name is SG")

class Company(Employee):
    def cmp_id(self):
        print("Company id is 1443")
    def cmp_name(self):
        print("Company name is React")

class Client():
    def client_id(self):
        print("Client id is 123")
    def client_name(self):
        print("Client name is Sura")

class Manager(Company,Client):
    def manager_id(self):
        print("Manager id is 1122")
    def manager_name(self):
        print("Manger name is SelvaG")

m=Manager()
m.manager_id()
m.manager_name()
m.client_id()
m.client_name()
m.cmp_id()
m.cmp_name()
m.emp_id()
m.emp_name()