pnum = input("Phone number: ")  #9841
map = {"0":"Zero","1":"One","2":"Two","3":"Three",
       "4":"Four","5":"Five","6":"Seven",
       "7":"Seven","8":"Eight","9":"Nine"}
output=""
for i in pnum:
    output=output + map.get(i)+" "
print(output+"!")
