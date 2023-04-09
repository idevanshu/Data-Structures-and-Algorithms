def constructRectangle(area):
    r = int(area**0.5)
    while True:
        y = area / r
        if y.is_integer():
            if r > y:
                return [r,int(y)]
            else:
                return [int(y),r]
        r -= 1

while True:
    x = int(input("Enter the number: "))
    print(constructRectangle(x))