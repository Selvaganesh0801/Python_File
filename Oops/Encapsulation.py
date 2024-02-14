class Employee():
    # Setter
    def setempid(self,empid):
        self.__empid=empid

    def  setempname(self,empname):
         self.__empname=empname

    def setempph(self,empph):
        self.__empph=empph

    # Getter
    def getempid(self):
        return self.__empid

    def getempname(self):
        return self.__empname

    def getempph(self):
        return self.__empph
e=Employee()
e.setempid(1234)
e.setempname("SelvaG")
e.setempph(1234567890)

a=e.getempid()
print(a)
print(e.getempname())
print(e.getempph())

# 2nd set of data
e1=Employee()
e1.setempid(143)
e1.setempname("SG")
e1.setempph(987654321)

print(e1.getempid())
print(e1.getempname())
print(e1.getempph())

#3rd set of data
e2=Employee()
e2.setempid(1443)
e2.setempname("Sekar")
e2.setempph(987612345)

print(e2.getempid())
print(e2.getempname())
print(e2.getempph())

# list
print("---------User defined list-------------")
l=[e,e1,e2]

a=l[0]
print(a.getempid())
print(a.getempname())
print(a.getempph())

a=l[1]
print(a.getempid())
print(a.getempname())

print("-------For loop-----------")

for i in range(0,len(l)):
    print(l[i].getempid())
    print(l[i].getempname())
    print(l[i].getempph())

for i in l:
    print(i.getempid())
    print(i.getempname())
    print(i.getempph() )
