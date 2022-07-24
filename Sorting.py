from array import *


def sor(num):
    result = 0
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j] > num[j+1]:
                result = num[j]
                num[j] = num[j+1]
                num[j+1] = result

    print(num)
    return num


size = int(input("Сколько элементов массива потребуется?: "))
numbers = array("i", [])
for i in range(size):
    numbers.append(int(input(f"Введите {i} число массива: ")))
print(numbers)
sor(numbers)
