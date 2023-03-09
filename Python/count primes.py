def countPrimes(n):
    if n == 0:
        return 0
    primes = [True for i in range(n+1)]
    count = 0
    factors = 2
    while factors * factors <= n:
        for i in range(factors * 2, n+1,factors):
            primes[i] = False
        factors += 1
    primes[0],primes[1] = False,False
    for p in range(n):
        if primes[p]:
            count += 1
    return count

while True:
    x = int(input("Enter the number: "))
    print(countPrimes(x))