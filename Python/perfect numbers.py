def checkPerfectNumbers(num):
    count = 0
    for i in range(1,int(num**(1/2))+1):
        if num % i == 0:
            count += i
            if i*i!=num:
                count+=num//i
    return count-num==num


while True:
    x = int(input("Enter a number: "))
    print(checkPerfectNumbers(x))