def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
while True:
    x = int(input("Enter a Number: "))
    print(fib(x))