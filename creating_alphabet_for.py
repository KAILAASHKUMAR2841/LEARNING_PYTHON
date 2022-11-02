num = [5,2,5,2,2]
for i in num:
    output = ""
    for j in range(i):
        output += "*"
    print(output)
print()

for i in num:
    print("+"*i)
