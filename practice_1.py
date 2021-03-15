class Human:
    """Attributes of the the Human (Human information)"""
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = int(age)
        self.height = float(height)
        self.weight = weight

    def sit(self):
        print(f"{self.name}, is sitting down on chair 10..".upper())

    def stand_up(self):
        print(f"{self.name}, is standing up".upper())

    def walk(self):
        print(f"{self.name}, is wants to walk but his weight is {self.weight} kg".upper())

    def describe(self):
        print(f"{self.name}, is {self.age} years old and his height: {self.height}".upper())


human1 = Human("chirag", 33, 5.5, 70)
human1.describe()
human1.walk()
print()

human2 = Human("mike", 40, 6.0, 99)
human2.describe()
human2.sit()