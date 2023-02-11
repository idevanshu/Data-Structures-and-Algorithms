import time

start = time.time()
def reverse(x):
    if x == 0:
        return 0
    elif x > 0:
        sign = 1
    else:
        sign = -1
        x = -x
    rev = 0
    while x > 0:
        if rev > 214748364 or (rev == 214748364 and x % 10 > 7):
            return 0
        rev = rev * 10 + x % 10
        x //= 10
    return sign*rev

end = time.time()

X = int(input("Enter the number: "))
print(reverse(X))
print("The time of execution of above program is :",(end-start) * 10**3, "ms")
