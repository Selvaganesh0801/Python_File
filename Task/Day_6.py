print("-----Function Task------")
# emp_Id(), emp_Name(), emp_Dob(), emp_Phone(), emp_Email(), emp_Address()

def fun():
    a=143
    b="SelvaG"
    c="8.1.2001"
    d=9488793821
    e="sg08012001@gmail.com"
    f="2/14,Thular"
    print("emp_Id:",a)
    print("emp_Name:"+b)
    print("emp_Dob:"+c)
    print("emp_Phone:",d)
    print("emp_Email:"+e)
    print("emp_Address:"+f)
fun()
print("-------------")
# greens_Omr(),greens_Adayar(),greens_Tambaram(),greens_Velacherry(),greens_Anna_Nagar()
def greens(a,b):
    c=a+b
    print(c)
greens('greens_Omr:','Branch-1')
greens('greens_Adayar:','Branch-2')
greens('greens_Tambaram:','Branch-3')
greens('greens_Velacherry:','Branch-4')
greens('greens_Anna_nagar:','Branch-5')
print("----------------")
# add(), sub()
def add(a,b):
    c=a+b
    print(c)
    return c
tot=add(20,30)
print(tot)

def sub(a,b):
    c=a-b
    print(c)
sub(50,30)

def cal(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a%b
    return add,sub,mul,div
tot=cal(2,4)
print(tot)
print("---------------")
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Harry","Potter")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# company_details(),employee_details()
def details(a,b):
    c=a+b
    return c
tot=details("company_details:Softeon","employee_details:SelvaG")
print(tot)
print(type(tot))
print("----------------")
# details(), names()
def det(a,b):
    c=a+b
    return c
tot=det("details:Working","names:Software")
print(tot)

def computer_names(*names):
  print(names)
computer_names("hp","sony","dell")
print(type(computer_names))


