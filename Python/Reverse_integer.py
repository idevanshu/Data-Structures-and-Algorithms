import time

start = time.time()

def reverse(x):
       
        if x < 0:
            z = x*-1
            y = str(z)[::-1]
            x = int(y)*-1

        else:
            y = str(x)[::-1]
            x = int(y)
        if x.bit_length() >= 32:
            return 0
        else:
            return x

end = time.time()

X = int(input("Enter the number: "))
print(reverse(X))
print("The time of execution of above program is :",(end-start) * 10**3, "ms")