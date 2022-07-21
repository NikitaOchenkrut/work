# Задача 1 - Простое число.

print('Введите натуральное число.')
n = input()
if int(n) < 0:
    print('Число не простое')
for num in range(int(n)+1):
    if num > 1:
        if int(n) % num == 0:
            if int(n) != num:
                print('Число не простое.')
                break
        else:
            print('Число простое.')
            break
    if int(n) == 2:
        print('Число простое.')
        break

# Задача 2 - Сумма десяти чисел
result = 0
for num in range(10):
    a = int(input("Введите число для сложения: "))
    if a < 0:
        print("Число не может быть отрицательным.")
        break
    else:
        result += a

print("Сумма десяти чисел равна: ", result)

# Задача 3 - Программа которая выводит
num = 1
for num in range(101):
    if num in (7, 17, 29, 78):
        continue
    else:
        print(num)

# Задача 4 - Что покажет код.
# Цикл от 0 до 10
for i in range(10):
#Вывод на экран числа с "*"
    print(i, end='*')
#Цикл прирывается когда i = 7 и выводит "0*1*2*3*4*5*6*7*"
    if i > 6:
        break
print(" ")
# Задача 5 - Программа «Симулятор ребенка»

while True:
    print("Почему?")
    answer = input()
    if answer == "покачану":
        print("Окидоки")
        break

# Задача 6 - Битва

name = input("Введите своё имя: ")
print(name, ",только ты сможешь победить андедов и спасти деревню.")
print("Полная готовность к бою?")
readiness = input()
live = 13
hit = 2
kills = 0
if readiness == "да":
    print("У вас 13 жизней.")
    while i:
        live -= hit
        kills += 1
        if live < 2:
            print(live, "жизней осталось,", kills, "убитых андедов.")
            break
        print(live, "жизней осталось,", kills, "убитых андедов.")
else:
    happy_end = input("Нажмите entr")

# Задача 7 - сумма чисел

try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a) + int(b)
except ValueError:
    print(a+b)
else:
    print(result)
