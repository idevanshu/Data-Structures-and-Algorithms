def climbStairs(n):
    if n <= 2:
        return n
    x = 1
    y = 2
    for i in range(2, n):
        temp = x
        x = y
        y = temp + x
    return y

while True:
    x = int(input("Enter a number: "))
    print(climbStairs(x))