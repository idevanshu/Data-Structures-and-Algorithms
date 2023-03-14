def isNumber(s):
    try:
        float(s)
    except:
        return False
    if 'nf' in s:
        return False
    return True

while True:
    x = str(input("Enter the characters: "))
    print(isNumber(x))