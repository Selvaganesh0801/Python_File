class Employee():
    def add(self,a,b):
        c=a+b
        print(c)
e=Employee()
e.add(10,20)
e.add(20,30)
e.add(25,25)

#Operator loading
# +
a=10
b=10
print(a+b)

a="ab"
b="cd"
print(a+b)

#Method overloading

class Employee():
    def emp_details(self,id):
        print("Employee id is",id)
    def emp_details(self,name):
        print("Employee name is",name)
    def emp_details(self,name,initial):
        print("employee name is",name,"Employee initial is",initial)
    def emp_details(self,id=None,name=None):
        print("Employee id is",id,"employee name is",name)

e=Employee()
# e.emp_details("SELVAG","K")
e.emp_details(123)
e.emp_details(123,"SelvaG")
e.emp_details(id=143)
e.emp_details(name="SelvaG")
e.emp_details(id=143,name="SelvaG")

#Method Overriding

class RbiBank():
    def savings(self,a):
        print("Savings 5%")
    def current(self):
        print("Current 6%")
    def fixed(self):
        print("Fixed 5%")
class GreensBank(RbiBank):
    def savings(self,a):
        print("Savings 6%")
    def current(self):
        print("Current 7%")
    def deposit(self):
        print("Deposit 4%")

g=GreensBank()
g.savings(143)
g.current()
g.deposit()
g.fixed()

r=RbiBank()
r.savings(143)
r.current()