def lengthOfLastWord(s):
    x = [i for i in s.split(" ")]
    y = []
    for i in x:
        if i == "":
            continue
        else:
            y.append(i)
    count = y[len(y)-1]
    return len(count)

print(lengthOfLastWord("luffy is still joyboy"))