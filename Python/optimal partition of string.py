def partitionString(s):
    count = 1
    subString = ""
    for i in s:
        if i not in subString:
            subString += i
        else:
            count += 1
            subString = i 
    return count 

print(partitionString("abacaba"))