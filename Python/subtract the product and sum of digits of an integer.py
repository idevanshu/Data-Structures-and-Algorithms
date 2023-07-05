def subtractProductAndSum(n):
    digits = list(str(n))
    sums = 0
    product = 1
    for i in digits:
        sums += int(i)
        product *= int(i)
    return product - sums

print(subtractProductAndSum(234))