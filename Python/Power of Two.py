def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n-1)) == 0

while True:
    n = int(input("Enter the number: "))
    print(isPowerOfTwo(n))