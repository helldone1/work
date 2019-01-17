# __author__ = 'Федоров Владислав Николаевич'

#Задача 1
fruits = [")Яблоко", ")Киви", ")Арбуз", ")Банан"]
i = 1
for fruit in fruits:
    str = "{}" "{}".format(i, fruit)
    print(str)
    i += 1

#Задача 2

office_buy = ['Мышка', 'Клавиатура', 'Монитор', 'Кресло', 'Колонки']
Broke_office = ['Системник', 'Кондиционер', 'Монитор', 'Колонки', 'Вебкамера']
print('Что купили в офис: {}'.format(office_buy))
print('Что сломалось в офисе: {}'.format(Broke_office))
for in_office in office_buy:
    for Broke_in_office in Broke_office:
        if Broke_in_office in office_buy:
            office_buy.remove(Broke_in_office)
print('Что осталось целым: {}'.format(office_buy))

#Задача 3

List = [150, 245, 390, 450]
for i in List[0:4]:
    if i % 2 == 0:
        print(i / 4)
    else:
        print(i * 2)