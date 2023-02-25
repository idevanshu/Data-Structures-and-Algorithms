def separateDigits(nums):
    jon = [str(i) for i in nums]
    numbers = "".join(jon)
    ret = [int(i) for i in numbers]
    return ret

print(separateDigits([13,25,83,77]))