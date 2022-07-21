class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def started(self):
        return "Автомобиль запущен"

    def finished(self):
        return "Автомобиль заглушен"

    def yearRelese(self):
        print("Год выпуска: {}".format(self.year))

    def color(self):
        print("Цвет: {}".format(self.color))

    def Type(self):
        print("Тип кузова: {}".format(self.type))
car1 = Car(color="Голубой", type= "Седан", year= "2005")
print(car1.Type(), car1.color(), car1.yearRelese())
print(car1.started(), "\n", car1.finished())
