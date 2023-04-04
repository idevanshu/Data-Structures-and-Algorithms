def splitNum(num):
    s = sorted(str(num))
    left = int(''.join(s[::2]))
    right = int(''.join(s[1::2]))
    return left + right

while True:
    x = int(input("Enter a number: "))
    print(splitNum(x))