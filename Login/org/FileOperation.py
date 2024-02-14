# file
f=open(r"C:\Users\VIJAY\PycharmProjects\Sample pro\Login\org\sample.txt","w")

# is file can be written
print(f.writable())
# is file has been read
print(f.readable())

# is it closed
print(f.closed)

# closed
print(f.close())
print(f.closed)

# write
# write str
# writeline-----list of str

f=open("sample.txt","w")
f.write("Welcome to html\t")
f.write("Welcome to css\n")
f.write("Welcome to js\t")

# writelines
f.writelines(["Welcome to Python\t","Welcome to Django\n","Welcome to C#\t"])

# append----mode---a
f=open("sample.txt","a")
f.write("\tSelvaG")

# read
# read()
# read(index)
# readline(index)
# readlines
print("__________________")
f=open("sample.txt","r")
# a=f.read()
# print(a)
# print(f.read())
# print(f.read(3))
print(f.read(20))

# w+ r+ a+
f=open("sample.txt","w+")
f.write("Hello Everyone")
f.write("\tWellcome")

print(f.readable())
# to find the particular of the cursor
print(f.tell())
print(f.read())

# seek--------to move the cursor from place to another
f.seek(0)
print(f.tell())
print(f.read())

# r+
f=open("sample.txt","r+")

print(f.read())
f.write("All")
f.seek(0)
print(f.read())

# a+-----write and read
f=open("sample.txt","a+")
f.write("\nWelcome")
f.write("Guys")

f.seek(0)
print(f.read())

f=open(r"C:\Users\VIJAY\PycharmProjects\Sample pro\Login\org\new.txt","w")
f=open("images (1).png","rb")
img=f.read()
print(type(img))

f1=open("img.jpg","wb")
f1.write(img)


f=open("dmo.png","rb")
img=f.read()
print(type(img))

s=open("dmo.png","wb")
s.write(img)
# -------------------
# csv
import csv
with open("ms.csv","w",newline="") as f:
    f1=csv.writer(f)
    f1.writerow(["100","Kumar","@gmail.com"])
    f1.writerow(["100","mar","mar@gmail.com"])
    f1.writerow(["100","Kum","kum@gmail.com"])

with open("ms.csv","r") as f:
    fr=csv.reader(f)
    print(fr)
    print(type(fr))
    l=list(fr)
    print(l)

for i in l:
    print(i)

for i in l:
    for j in i:
        print(j)
    print()

# zipfile write

from zipfile import *
# with ZipFile("all.zip","w",ZIP_DEFLATED) as f:
#      f.write("sample.txt")
#      f.write("new.txt")
#      f.write("ms.csv")
#      f.write("dmo.png")
#      f.write("img.jpg")

with ZipFile("allfile.zip","w",ZIP_DEFLATED) as f:
    f.write("sample1.txt")
    f.write("sample2.txt")
    f.write("sample3.txt")

# zipfile.read
# with ZipFile("allfile.zip","r",ZIP_STORED) as f:
#     f1.f.namelist()
#     print(type(f1))
#     print(f1)

# for i in f1:
#     print(i)
#
# for i in f1:
#     o=open(i,"r")
#     print(o,read())

# folder
import os
# create folder----can create new folder at a time
# fl=os.mkdir("python")
# fl=os.mkdir("Java")
# fl=os.mkdir(r"Java/new")
# fl=os.mkdir(r"Java/new/a")
# fl=os.mkdir(r"Java/new/a/b")
# fl=os.mkdir(r"Java/new/a/b/c")

# subfolder---------makedirs
# fl=os.makedirs(r"Python/new/A/B/C")

# print all the folder
ls=os.listdir("java")
print(ls)
print(type(ls))

# can get all the subfolder
l=os.walk("java")
print(l)
print(type(l))

li=list(l)
print(li)
print()
for i in li:
    print(i)

file="sample.txt"
dir="python"

# file
f1=os.path.isfile(file)
print(f1)
print(type(f1))

f1=os.path.isfile(dir)
print(f1)
print(type(f1))
print()
# isdir
f1=os.path.isdir(file)
print(f1)
print(type(f1))

f1=os.path.isdir(dir)
print(f1)
print(type(f1))

# redir
# os.rmdir("python")
# os.rmdir("Java/new/a")