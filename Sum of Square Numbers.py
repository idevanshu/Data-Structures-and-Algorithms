def judgeSquareSum(c):
    i = 0
    j = int(c**0.5)
    for i in range(i,j+1):
        for j in range(i,j+1):
            print(f"{i*i} + {j*j} = {i*i + j*j}" )
            if i*i + j*j == c:
                return True
    return False
while True:
    x = int(input("Enter the number: "))
    print(judgeSquareSum(x))