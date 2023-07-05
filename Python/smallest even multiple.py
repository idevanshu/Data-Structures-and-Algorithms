def smallestEvenMultiple(n):
    i = 1
    if n % 2 == 0: return n 
    while True:
        if i % n == 0 and i % 2 == 0:
            return i
        else: 
            i += 1

print(smallestEvenMultiple(6))
print(smallestEvenMultiple(5))