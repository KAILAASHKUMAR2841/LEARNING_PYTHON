class Mammal:
    def __init__(self,x):
        self.x1 = x
    def walk(self):
        print("WALKING")
class Dog(Mammal):
    def bark(self):
        print(f"BARKING {self.x1}")
class Cat(Mammal):
    def annoy(self):
        print(f"ANNOYING {self.x1}")
dog1 = Dog("DOG")
dog1.walk()
dog1.bark()

cat1 = Cat("CAT")
cat1.walk()
cat1.annoy()


