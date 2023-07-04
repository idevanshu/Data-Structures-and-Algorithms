def singleNumber(nums):
    nums.sort()
    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i+1]:
            return nums[i]
        i += 3
    return nums[-1]
    
print(singleNumber([0, 1, 0, 1, 0, 1, 99])) 