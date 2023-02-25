
def mysqrt(x):
    sqrt = x**(1/2)
    return int(sqrt)


while True:
    x = int(input("Enter the number: "))
    print(mysqrt(x))