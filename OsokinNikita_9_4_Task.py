class TriangleChecker:
    pass

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def is_triangle(self):
        if not self.A.isdigit() or not self.B.isdigit() or not self.C.isdigit():
            print("Нужно вводить только числа!")
        elif int(self.A) > 0 and int(self.B) > 0 and int(self.C) > 0:
            if int(self.A) <= int(self.C) and int(self.B) <= int(self.C) and (int(self.A) + int(self.B)) > int(self.C):
                print("Ура, можно построить треугольник!")
            elif int(self.C) <= int(self.A) and int(self.B) <= int(self.A) and (int(self.C) + int(self.B)) > int(self.A):
                print("Ура, можно построить треугольник!")
            elif int(self.A) <= int(self.B) and int(self.C) <= int(self.B) and (int(self.A) + int(self.C)) > int(self.B):
                print("Ура, можно построить треугольник!")
            else:
                print("Жаль, но из этого треугольник не сделать.")
        elif int(self.A) <= 0 or int(self.B) <= 0 or int(self.C) <= 0:
            print("С отрицательными числами ничего не выйдет!")



TR1 = TriangleChecker(A=input("Первая сторона треугольника: "), B=input("Вторая сторона треугольника: "), C=input("Третья сторона треугольника: "))
print(TR1.is_triangle())
