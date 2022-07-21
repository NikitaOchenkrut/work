class RealString:

    def __init__(self, string_one, string_two):
        self.string_one = string_one
        self.string_two = string_two

    def who_is_bigger(self):
        print(len(self.string_one))
        print(len(self.string_two))
        if len(self.string_one) > len(self.string_two):
            print(f"Первый объект больше втрого на {int(len(self.string_one))-int(len(self.string_two))} символов")
        elif len(self.string_two) > len(self.string_one):
            print(f"Первый объект больше втрого на {int(len(self.string_two)) - int(len(self.string_one))} символов")
        else:
            print("У объектов одинаковое количество символов")

exemple = RealString(string_one=input("Введите первый объект: "), string_two=input("Введите второй объект: "))
print(exemple.who_is_bigger())
