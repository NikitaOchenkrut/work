def isEven(value):
    if value % 2 == 0:

        return f"Число {value} четное."
    else:
        return "Введенное число нечетное"

number = input("Введите число: ")
print(isEven(int(number)))