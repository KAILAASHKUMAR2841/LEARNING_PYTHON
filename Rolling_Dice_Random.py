import random

class Dice():
  def roll(self):
    first = random.randint(1,7)
    second = random.randint(1,7)
    return (first,second)


spin = Dice()
print(spin.roll())
