def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)":"😁",
        ":(":"😒",
        "luv":"❤"
    }
    output=""
    for i in words:
        output+=emoji.get(i,i)+" "
    return output


message = input(">")
emoji_converter(message)
print(emoji_converter(message))
