# oops Concepts:--
# class classname():   ().........optional
# def methodname():

class EmployeeDetails():
    def employee_name(self):
        print("Employee name is SelvaG")

    def employee_id(self):
        print("Employee id is 143")

# object creation
# var=classname()
a=EmployeeDetails()

# method calling
# objname.methodname
a.employee_name()
a.employee_id()

print("________________________")

class EmployeeDetails():
    def employee_name(self):
        print("Employee name is Ganesh")
    def employee_id(self):
        print("Employee id is 1443")

a=EmployeeDetails()
print(id(a ))
a.employee_id()
a.employee_name()
print("________________________")
b=EmployeeDetails()
print(id(b))
b.employee_id()
b.employee_name()
print("________________________")

class EmployeeDetails():
    def employee_name(self,name):
        print("Employee name is ",name)
        print(id(name))
    def empolyee_id(self):
        print("Employee id is 143")
        print(id(self))

a=EmployeeDetails()
print(id(a))
a.empolyee_id()
a.employee_name("SelvaG")
print("________________________")


