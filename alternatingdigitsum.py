def alternateDigitSum(n):
    count = 0
    digits = []
    for i in str(n):
        count += 1
        if count % 2 != 0:
            digits.append(int(i))
        else:
            digits.append(int(i)*-1)
    
    return sum(digits)


while True:
    x = int(input("Enter the number: "))
    print(alternateDigitSum(x))