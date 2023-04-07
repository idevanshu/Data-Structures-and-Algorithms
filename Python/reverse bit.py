def reverseBits(n):
        reverse = 0
        for i in range(32):
            reverse = (reverse << 1) | (n & 1)
            n >>= 1
        return reverse

while True:
    x = int(input("Enter a number: "))
    print(reverseBits(x))