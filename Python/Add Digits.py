def add_digits(num):
    while num >=10:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum
    return num

while True:
    num = int(input("Enter the number: "))
    print(add_digits(num))