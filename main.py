import random


class Student:
    def __init__(self, name=None, age=None, money=100):
        self.name = name
        self.age = age
        self.money = money
        self.stress = 0
        self.knowledge = 0
        self.month = 1

    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."

    def work(self):
        print(f"{self.name} is working.")
        self.money += random.randint(50, 100)
        self.stress += 5

    def study(self):
        print(f"{self.name} is studying.")
        self.knowledge += random.randint(5, 15)
        self.stress += 10

    def rest(self):
        print(f"{self.name} is resting.")
        self.stress -= 15
        self.money -= random.randint(10, 30)

    def monthly_check(self):
        if self.money < 50:
            print(f"{self.name} doesn't have enough money, time to work!")
            self.work()
        elif self.stress > 50:
            print(f"{self.name} is too stressed, time to rest!")
            self.rest()
        elif self.knowledge < 50:
            print(f"{self.name} needs to study more!")
            self.study()
        else:
            action = random.choice([self.work, self.study, self.rest])
            action()

    def live_year(self):
        while self.month <= 12:
            print(f"\nMonth {self.month}:")
            self.monthly_check()
            self.month += 1
            print(f"Money: {self.money}, Knowledge: {self.knowledge}, Stress: {self.stress}")


vasya = Student("Vasya", 20)

print(vasya.introduce())
vasya.live_year()
