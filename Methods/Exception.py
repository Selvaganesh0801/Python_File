# Excception Handling
# ZeroDivisionError:
print(1)
print(2)
print(3)
# print(4/0)   #ZeroDivisionError:
print(5)

from builtins import Exception
# TypeError
print(1+1)
print("1"+"2")
# print("1"+2)     TypeError

# ValueError
print(int(10))
print(int("10"))
# print(int("Ten"))    ValueError

# IndexError
l=[10,20,30,40,50]
print(l[1])
# print(l[6])     IndexError

# try------line of error
# except-----solution
print('------------------')
# try with exception
print(1)
print(2)
print(3)
try:
    print(4/0)
except ZeroDivisionError:
    print("Zero")
print('------------------')
# try except with parent class
print(1)
print(2)
print(3)
try:
    print(4/0)
except BaseException:
    print("Base")
print('------------------')
# to know which kind of exception
print(1)
print(2)
print(3)
try:
    print("1"+0)
except BaseException as e:
    print("Parent")
    print(e)
print(5)
print('------------------')
# default exception
print(1)
print(2)
print(3)
try:
    print("1"+0)
except:
    print("Default")
print(5)
print('------------------')
# try with multiple exception
print("Start")
try:
    print(l[7])
except TypeError:
    print("Type")
except ValueError:
    print("Value")
except ZeroDivisionError:
    print("Zero")
except IndexError:
    print("Index")
except:
    print("Default")
print("Stop")

# hierrachy it means work by one by one line it did'nt consider the second line
print("--------------------------")
# try except finally------it didn't handling declare error only
print("Start")
try:
    print(1/0)
except ZeroDivisionError:
    print("I am in Except")
finally:
    print("I am in Finally")
print("End")

# try & finally
# print("Start")
# try:
#     print(1/0)
# finally:
#     print("Finally")
# print("End")
print("----------------------------")
# try,except,else,finally
print("Start")
try:
    print(1)
except ZeroDivisionError:
    print("Except")
else:
    print("Else")
finally:
    print("Finally")
print("----------------------------")
# raise----we can used raise to bring up 0 error when we want
# productname=input("Enter ur model:")
#
# if productname=="Iphone":
#     print("Product Available")
# else:
#     print("Product Not Available")
#     raise ValueError
print("----------------------------")
class ProductNotAvailable(Exception):
    msg="Sale"

# user defined error or exception---we have to create a class
# productname=input("Enter ur module")
#
# if productname=="Oneplus":
#     print("Product Available")
# else:
#     print("Product Not Available")
#     raise ProductNotAvailable
print("----------------------------")

# exception handling
# productname=input("Enter ur model:")
# if productname=="iphone":
#     print("Product Available")
# else:
#     print("Product Not Available")
#     try:
#         raise ProductNotAvailable
#     except:
#         print("Handled")
# print("stop")


# productname=input("Enter ur model:")
# if productname=="iphone":
#     print("Product Available")
# else:
#     print("Product Not Available")
#     try:
#         raise ProductNotAvailable
#     except ProductNotAvailable as e:
#         print("Handled")
#         print(e.msg)
# print("stop")

# except with multiple exception
print("Start")
try:
    print(4/0)
except(TypeError,ZeroDivisionError,ValueError):
    print("SelvaG")
print("End") 