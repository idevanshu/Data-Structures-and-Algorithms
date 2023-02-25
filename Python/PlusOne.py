def plusOne(digits):
    new = [str(i) for i in digits ]
    print(new)
    to_int = int("".join(new))
    final = to_int + 1
    ans = [int(i) for i in str(final) ]
    return ans
print(plusOne([1,2,3]))