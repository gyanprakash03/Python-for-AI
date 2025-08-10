list = ["hello", "everyone", "one", "hell", "phone"]

def rem(list, word):
    new = []
    for i in range(len(list)):
        if (word in list[i]):
            el = list[i].replace(word, "")
            if el != "":
                new.append(el)
        else:
            new.append(list[i])

    return new

print(rem(list, "one"))