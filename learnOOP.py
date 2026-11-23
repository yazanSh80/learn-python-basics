class LearnOOP:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age} years old")


person1 = LearnOOP("Yazan", 23)

person1.introduce()

def counter():
    count =1
    while count<10:
        count *= 2
        print("count :",count)


counter()