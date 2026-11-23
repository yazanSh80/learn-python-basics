from Dog import Dog


class Main:
    def run(self):
        dog1 = Dog("Max", 3)

        dog1.introduce()
        dog1.bark()
        dog1.eat("Chicken")


main = Main()
main.run()