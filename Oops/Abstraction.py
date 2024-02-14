from abc import ABC,abstractmethod
class RbiBank(ABC):
    @abstractmethod
    def savings(self):
        pass
    @abstractmethod
    def current(self):
        pass
    def fixed(self):
        print("Fixed 5%")

# r=RbiBank()
# r.savings()
# r.current()
# r.fixed()

class GreensBank(RbiBank):
    def savings(self):
        print("Savings 6%")
    def current(self):
        print("Current 7%")
    def deposit(self):
        print("Deposit 4%")

g=GreensBank()
g.savings()
g.current()
g.deposit()
g.fixed()

#public
class Employee():
    def emp_id(self):
        self.empid=143
        print(self.empid)
e=Employee()
e.emp_id()

#Private
class Employee():
    def __emp_id(self):
        self.__empid=123
        print(self.__empid)
    def emp_name(self):
        self.__emp_id()

e=Employee()
e.emp_name()


