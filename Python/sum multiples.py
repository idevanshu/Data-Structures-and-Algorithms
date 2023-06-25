def sumOfMultiples(n):
        num = []
        for n in range(1,n+1):
            if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
                num.append(n)
        
        return sum(num)

print(sumOfMultiples(100))