def countSpecialNumbers(n):
    count = 0
    for i in range(1, n + 1):
        numbers = set()
        for char in str(i):
            if char in numbers:
                break
            numbers.add(char)
        else:
            count += 1
    return count

while True:
    n = int(input("Enter a number: "))
    countSpecialNumbers(n)