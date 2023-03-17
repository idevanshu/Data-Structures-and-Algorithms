
def isPowerOfThree(n):
    if (n <= 0):
        return False
    if (n % 3 == 0):
        return isPowerOfThree(n // 3)
    if (n == 1):
        return True
    return False

while True:
    x = int(input("Enter a number: "))
    print(isPowerOfThree(x))