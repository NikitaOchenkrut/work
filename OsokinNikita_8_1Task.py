import math
import time
# Задача 1 - простая арифметика
def arithmetic():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    operation = input('Какую операцию нужно произвести над числом? ')
    if operation == '-':
        return a-b
    elif operation == '+':
        return a + b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b
    else:
        print('Неизвестная операция.')
        return None
print(arithmetic())

# Задача 2 - Високосный год
def is_year_leap(years):
    if years % 4 == 0:
        if years % 400 == 0:
            return True
        elif years % 100 == 0:
            return False
        else:
            return True

    else:
        return False
years = int(input('Введите год: '))
print(is_year_leap(years))

# Задача 3 - Операция над квадратом
def square():
    long = int(input('Чему равна сторона квадрата? '))
    perimeter = long*4
    new_square = long**2
    diagonal = math.sqrt(2*new_square)
    result = [perimeter, new_square, diagonal]
    result = tuple(result)
    return result
print(square())
# Задача 4 - расскажи мне про время года
def season():
    month = int(input('Введите номер месяца '))
    if month < 1:
        print('Такого месяца не существует')
        return
    elif month > 12:
        print('Такого месяца не существует')
        return
    elif month < 3 or month > 11:
        return 'За окном идет снег, видимо зима '
    elif month < 6:
        return 'Люди вокруг начинают чихать, время весны'
    elif month < 9:
        return 'Да да наступили те самые лучшие и долгожданные дни по российским меркам, это лето'
    else:
        return 'В воздухе запахло лирикой(и это я не про сектор газа), это осень'

print(season())

# Задача 5 - Банк
def bank():
    a = int(input('Введите сумму вклада... '))
    years = int(input('На сколько лет делаем вклад? '))
    print('Вклад будет расчитан по ставке 10 % годовых')
    procent = 0
    i = 0
    for i in range(years):
        procent = a * 0.1
        a += procent
        i += 1
    if years > 4:
        print('За', years, 'лет ваш вклад составит ... ')
    elif years > 1:
        print('За', years, 'года ваш вклад составит ... ')
    else:
        print('За', years, 'год ваш вклад составит ... ')
    time.sleep(2)
    return round(a, 2)
print(bank())

# Задача 6 - Дата

def date():
    years = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    if 1 > day > 31:
        return False
    elif 1 > month > 12:
        return False
    elif years < 0:
        return False
    elif month == 2:
        if 1 < day < 29:
            return True
        if day == 29:
            if is_year_leap(years) == True:
                return True
            else:
                return False
        elif day > 28:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return False
        else:
            return True
    else:
        return True
print(date())

# Задача 7 - Ключ

my_string = (input('Введите строку которую нужно зашифровать: '))
my_key = int(input('Задайте шифр: '))
def XOR_cipher():
    # Функция зашивровывает строку
    new_my_string = int(len(my_string) ^ my_key)
    print(new_my_string)
    return my_key
print(XOR_cipher())

exam_my_key = int(input('Введите правильны ключ: '))
def XOR_uncipher():
    # Функция расшивровывает данные при правильном шифре
    if exam_my_key == my_key:
        return my_string
    else:
        return None
print(XOR_uncipher())
