#guesing game
sec_num = 7
index = 1
while (index < 4):
    guess = int(input("Guess: "))
    index += 1
    if(guess == sec_num):
        print("You WON!")
        break
else:
    print("You LOST!")
