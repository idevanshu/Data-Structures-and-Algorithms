def missingNumber(nums):
    new = []
    for i in range(len(nums)):
        new.append(i+1)
    for i in new:
        if i not in nums:
            return int(i)
    
    return 0

print(missingNumber([3,0,1]))