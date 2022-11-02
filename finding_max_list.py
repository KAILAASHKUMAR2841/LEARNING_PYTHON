#TYPE 1
list = [1,5,7,2,3,4]
max = list[0]
for i in list:
    if i > max:
        max = i
print(max)

#TYPE 2
any = max(list)
print(any)
