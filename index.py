
# -*- coding: utf-8 -*-

import datetime

date = datetime.date.today()

#print(date.strftime('year: %Y'))




count_month = 12
pre_code_month = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]
pre_code_century = [6, 4, 2, 0]
str_dayweek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def get_code_age():
    year = date.year
    ind = int(year / 100 % 4)
    return pre_code_century[ind]
def get_code_year(year = date.year):
    #Код года = (6 + последние две цифры года + последние две цифры года / 4) % 7
    
    num = year % 100
    return (get_code_age() + num + num / 4) % 7
def get_code_month(month):
    year = date.year
    month -= 1

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        if month == 0 or month == 1:
            return pre_code_month[month] - 1
        else:
            return pre_code_month[month]
    else:
        return pre_code_month[month]
def get_dayweek(day = date.day, month = date.month, year = date.year):
    # День недели = (день месяца + код месяца + код года) % 7

    return int((day + get_code_month(month) + get_code_year(year)) % 7)

print(get_dayweek(1, 7, 2024))
    
# for i in range(1, 12 + 1):
#     print(get_code_month(i), end=" ")

# print()

def count_days_in_month(num_month):
    if num_month <= 7:
        if num_month % 2 != 0:
            return 31
        elif num_month == 2:
            year = date.year
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 30
    elif num_month % 2 == 0:
        return 31
    else:
        return 30
def count_days_in_year():
    sum = 0
    for i in range(1, 13):
        sum += count_days_in_month(i)
    return sum
def get_worknhol_days(month = date.month, year = date.year):
    count_day = count_days_in_month(month)
    num = count_day - 28
    X = 20
    Y = 8
    for i in range(get_dayweek(1, month, year), get_dayweek(1, month, year) + num):
        if i % 7 < 2:
            Y += 1
        else:
            X += 1
    return X, Y

# print(*get_worknhol_days())
# print(count_days_in_year())

# for i in range(1, count_days_in_month(date.month) + 1):
#     print(i, end=" ")

# for i in range(1, 13):
#     print(count_days_in_month(i))
