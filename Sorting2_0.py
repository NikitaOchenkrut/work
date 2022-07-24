

def sor(num):
    sorted(num)
    print(num)
    return


size = int(input("Сколько элементов массива потребуется?: "))
numbers = []
for i in range(size):
    numbers.append(int(input(f"Введите {i} число массива: ")))
print(numbers)
sor(numbers)
print(numbers)

