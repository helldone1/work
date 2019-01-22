__author__ = 'Федоров Владислав Николаевич'

#Задача 1

def convert(km):
    miles = km*1.609
    print(miles)
convert(367)

#Задача 2

def my_round(number, ndigits):
 number = number*(10**ndigits)+0.41
 number = number//1
 return number/(10**ndigits)
print(my_round(5435225.45646654, 5))

#Задача 3

def lucky_ticket(num):
 num=(list(map(int, list(str(num)))))
 if sum(num[:3]) == sum(num[3:]):
  print("True")
 else:
  print("False")
 return num
ticket=lucky_ticket(123321)