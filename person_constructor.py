class Person:
    def __init__(self,name):
        self.new = name
    def talk(self):
        print(f"Hi, I am {self.new}")
    def hear(self):
        print("HEARING "+self.new)


person1 = Person("KAILAASH")
person1.talk()
person1.hear()
person2 = Person("JOHNNY")
person2.talk()
