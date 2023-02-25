

def isPerfectSquare(num):
    sqrt = num**(0.5)
    number = int(sqrt)
    square_root = number * number

    if sqrt == number:
        if square_root == num:
            return True
        else:
            return False
    else:
        return False
    

while True:
    x = int(input("Enter the number: "))
    print(isPerfectSquare(x))