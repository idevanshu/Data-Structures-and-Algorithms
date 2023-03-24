def countTriples(n):
    count = 0
    i = 1

    while i <= n:
        x = 1
        while x < i:
            y = int((i**2 - x**2)**0.5)
            if y < x:break
            if y <= n and y**2 == i**2 - x**2:
                count +=2
            x += 1
        i += 1         
    return count

while True:
    x = int(input("Enter the number: "))
    print(countTriples(x))