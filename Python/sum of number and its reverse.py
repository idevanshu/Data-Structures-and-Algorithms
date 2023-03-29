def sumOfNumberAndReverse(num):
    if num == 0:return True
    i = 0
    while i < num // 2:
        if i + int(str(i)[::-1]) == num:
            return True
        i+=1
    return False


while True:
    x = int(input("Enter a number: "))
    print(sumOfNumberAndReverse(x))
