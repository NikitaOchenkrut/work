class Nikola:
    name = "Николай"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_name(self):
        if str(self.name) != "Николай":
            print(f"Я не {self.name}, а Николай")
            print(f"Возраст: {self.age}")
            self.name = "Николай"
        else:
            print(f"Имя: {self.name}")
            print(f"Возраст: {self.age}")

user1 = Nikola(name= input("Введите имя: "), age= input("Введите возраст: "))
print(user1.my_name())
print(user1.my_name())
