import string
def myAtoi(s):
    sign = 1
    if s and (s[0] == '-' or s[0] == '+'):
        sign = -1 if s[0] == '-' else 1
        s = s[1:]
    num = 0
    for i in s:
        if i.isdigit():
            num = num*10 + int(i)
        else:
            break
    num *= sign
    num = max(min(num, 2**31-1), -2**31)
    return num
    

while True:
    x = str(input("Enter the number: "))
    print(myAtoi(x))