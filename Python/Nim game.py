def canWinNim(n):
    return n % 4 != 0


while True:
    x = int(input("Enter a number: "))
    print(canWinNim(x))