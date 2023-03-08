def happy(n):
    visit = []

    def sumofsquare(num):
        number = 0
        for i in str(num):
            number += int(i)**2
        return number

    while n not in visit:
        visit.append(n)
        n = sumofsquare(n)
        if n == True:
            break

    if n == True:
        return True

    return False

while True:
    x = int(input("Enter the number: "))
    print(happy(x))