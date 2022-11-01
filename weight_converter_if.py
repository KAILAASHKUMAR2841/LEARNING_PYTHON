weight = input("Enter your weight: ")
cred = input("(L)bs or (K)gs: ")
if (cred == "l" or cred == "L"):
    lbs= int(weight)*0.45
    print(f"Your weight is {round(lbs)} kgs")
elif (cred == "k" or cred=="K"):
    kgs = int(weight)/0.45
    print(f"Your weight is {kgs} lbs")
