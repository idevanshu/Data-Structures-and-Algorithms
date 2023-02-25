def divide(dividend, divisor):
    x = dividend/divisor
    if x >= 2 ** 31 - 1:
        return 2**31 -1
    elif x <= -2 ** 31:
        return -2 ** 31
    else:
        return int(x)


print(divide(-2147483648
,-1))
