name = input("Enter your name: ")
if len(name)<3:
    print("Name must be atleast 3chars")
elif len(name)>50:
    print("Name can only be 50chars")
else:
    print("Looks good!")
