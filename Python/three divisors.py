def isThree(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count == 3

while True:
    x = int(input("Enter a number: "))
    print(isThree(x))