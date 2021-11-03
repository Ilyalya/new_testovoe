class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Auto:
    def __init__(self, name, year, probeg, model, owner):
        self.name = name
        self.year = year
        self.probeg = probeg
        self.model = model
        self.owner = owner

    def info(self):
        print("Автомобиль:" + self.name, self.model, self.year, "года выпуска,", "с пробегом", self.probeg, "км",
              "владелец: " + self.owner)


p1 = Person("Илья", 23)
machine = Auto("Bmw", 2021, 10000, 'x5', p1.name)
machine.info()