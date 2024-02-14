date="16-11-2023"
print(date)

import datetime

a=datetime.datetime.now()
print(a)
print(type(a))

d=datetime.datetime.today()
print(d)

print()

print(d.year)
print(d.month)
print(d.date())
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)

print("-----YEAR-----")
# print("%y")
# print("%Y")

print(d.strftime("%y"))  #year last 2 digit
print(d.strftime("%Y"))

print("----MONTH----")
print(d.strftime("%b"))
print(d.strftime("%B"))#----Letter
print(d.strftime("%m"))#-----number

print("----DATE----")
print(d.strftime("%a"))
print(d.strftime("%A"))
print(d.strftime("%d"))

print("----HOURS----")
print(d.strftime("%I"))#12hr
print(d.strftime("%H"))#24hr
print(d.strftime("%p"))


print("----MINUTES----")
print(d.strftime("%M"))

print("----SECONDS----")
print(d.strftime("%S"))

print("----MICRO_SECONDS----")
print(d.strftime("%f"))

# to create our own format
print(d.strftime("%d-%m-%Y"))
print(d.strftime("%H:%M:%S:%f"))

dv=datetime.datetime(2023,11,6)
print(dv)
print(type(dv))

dm=datetime.timedelta(days=100)
print(dm)
print(dv+dm )