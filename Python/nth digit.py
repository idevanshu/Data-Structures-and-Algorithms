def findNthDigit(n):
    """
    count = 0
    digit = 0
    for i in range(1, n +1):
        count += len(str(i))
        if count >= n:
            digit = int(str(i)[-(count - n + 1)])
            break
    return digit
    """
    count = 0
    length = 1

    while n > 9 * length * 10**(length-1):
        count += 9 * length * 10**(length-1)
        length += 1

    num = (n - count - 1) // length + 10**(length-1)
    digit_pos = (n - count - 1) % length

    return int(str(num)[digit_pos])

print(findNthDigit(1000000000))
