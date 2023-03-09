def isUgly(n):
    check = [2,3,5]
    if n <= 0:
        return False
    
    for i in check:
        while n % i == 0:
            n = n // i
    return n == 1
    
while True:
    x = int(input("Enter a number: "))
    print(isUgly(x))