# -*- coding: utf-8 -*-

import datetime

def age_calculator(input_dob):
    dob = disectDateString(input_dob)
    day_of_birth = dob[0]
    month_of_birth = dob[1]
    year_of_birth = dob[2]
    
    current_year, current_month, current_day = getToday()
    years = current_year-year_of_birth
    age = 0
    if current_month <= month_of_birth and current_day <= day_of_birth:
        age += years-1
    elif current_month == month_of_birth and current_day > day_of_birth:
        age = years
    elif current_month < month_of_birth:
        age += years-1
    elif current_month > month_of_birth:
        age += years
    return age

def getToday():
    current_year = int(datetime.datetime.now().strftime("%Y"))
    current_month = int(datetime.datetime.now().strftime("%m"))
    current_day = int(datetime.datetime.now().strftime("%d"))
    return current_year, current_month, current_day

def disectDateString(input_date):
    empty = ''
    date = []
    for char in input_date:
        if char != '/':
            empty += char
        elif char == '/':
            date.append(int(empty))
            empty = ''
    date.append(int(empty))
    return date

input_dob = input("Please enter D.O.B. dd/mm/yyyy: ")
age = age_calculator(input_dob)
print("Person is " + str(age) + " years old")