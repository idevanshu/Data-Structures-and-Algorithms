def selfDividingNumbers(left,right):
    result = []
    for i in range(left,right+1):
        for digit in str(i):
            if int(digit) == 0 or i % int(digit) > 0:
                break
        else:
            result.append(i)
    return result


print(selfDividingNumbers(left=1,right=22))