list = [1,5,5,5,5,7,7,7,4,5,6,9]
newl = []
for i in list:
  if i not in newl:
    newl.append(i)
print(newl)
