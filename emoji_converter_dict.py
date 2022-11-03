message = input(">")
words = message.split(" ")
emoji = {
    ":)":"😁",
    ":(":"😒",
    "luv":"❤"
}
output=""
for i in words:
    output+=emoji.get(i,i)+" "
print(output)
