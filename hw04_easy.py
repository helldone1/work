__author__ = 'Федоров Владислав Николаевич'

# Задача 1

lst1 = [1, 2, 4, 8, 0]
lst2 = [x**2 for x in lst1]
print(lst2)

#Задача 2

listfruit1 = ["Манго", "Арбуз", "Яблоко"]
listfruit2 = ["Манго", "Апельсин", "Папайа", "Яблоко"]
listfruit_union = [x for x in listfruit1 if x in listfruit2] if len(listfruit1)>len(listfruit2) else [x for x in listfruit2 if x in listfruit1]
print(listfruit_union)

#Задача 3

list_one = [1, 4, 6, 9, 0, -3, 15, -23, -11]
list_two = [el for el in list_one if el % 3 == 0 and el >=0 and el % 4 !=0]
print(list_two)
