from array import *


# Первая задача
lst = [5, 6, 3, 4, 1, 8, 9, -6, -9, -1]


def more_than_five(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] > 5 or lst[i] < -5:
                result.append(lst[i])
    print(result)
    return result
more_than_five(lst)

# Вторая задача
number = [6]


def is_divisible_by_6(number):
    i = 0
    while i != -1:
        if number[i] % 6 == 0:
            print('Число', number[i], ' делится на 6')
        else:
            print('Число ', number[i], ' не делится на 6')
        i -= 1
is_divisible_by_6(number)

# Третья задача
word = input("Введите что-нибудь с клавиатуры.")

if word == " ":
    print("")
else:
    print("OK")

# Четвёртая задача
number_ex = input("Введите число: ")
int(number_ex)
if int(number_ex) > 0:
    print("1")

else:
    print("-1")


# Пятая задача
num = 2
i = 0
while i < 20:
   print(pow(num, i))
   i += 1

# Шестая задача
i = 0
result = 0
while i < 101:
    result = result + i
    i += 1


print(result)

# Седьмая задача

i=0
result = 1
while i <= 9435:
    if i % 2 != 0:
        result = result * i
    i += 1
print(result)

# Восьмая задача

i = 54
my_array = array('i', [])
while i <= 9184:
    if i % 5 == 0:
        my_array.append(i)
    i += 1
# Вывел массив для проверки
print(my_array)

# Дополнительная задача с поиском натурального числа.
lower = int(input('Введите число с которого начнем счёт: '))
upper = int(input('Введите число которым закончим счёт: '))

print('Диапазон чисел между', lower, 'и', upper)

for number in range(lower, upper + 1):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)
           