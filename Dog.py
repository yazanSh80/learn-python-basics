class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("HAW HAW")

    def eat(self, food):
        print("The food is: " + food)

    def introduce(self):
        print("My name is " + self.name)
        print("My age is " + str(self.age))