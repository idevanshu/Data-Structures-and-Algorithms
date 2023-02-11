def sumDigits(no):
    return 0 if no == 0 else int(no % 10) + sumDigits(int(no / 10)) 
def countEven(num):
    count = 0
    for i in range(1,num+1):
        if sumDigits(i) % 2 == 0:
            count += 1

    return count

while True:
    n = int(input("Enter the number: "))
    print(countEven(n))