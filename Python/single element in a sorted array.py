def singleNonDuplicate(nums):
    n = len(nums)
    for i in range(0, n-1, 2):
        if nums[i] != nums[i+1]:
            return nums[i]
    return nums[-1]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))