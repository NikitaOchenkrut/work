class Math:

    def __init__(self, A, B):
        self.A = A
        self.B = B

    def addition(self):
        return self.A + self.B

    def multiplication(self):
        return self.A * self.B

    def division(self):
        if self.B == 0:
            return "На ноль делить нельзя."
        else:
            return self.A / self.B

    def subtraction(self):
        return self.A - self.B

num1 = Math(int(input("Введите первое число: ")), int(input("Второе число: ")))
print("Умножение чисел: ", num1.multiplication())
print("Деление чисел: ", num1.division())
print("Сложение чисел: ", num1.addition())
print("Разность чисел: ", num1.subtraction())


