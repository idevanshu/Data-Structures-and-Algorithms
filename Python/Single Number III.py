def singleNumber(nums):
    nums.sort()
    #Logic
    """
    final = []
    i = 0
    while i < len(nums):
        if i == len(nums)-1 or nums[i] != nums[i+1]:
            final.append(nums[i])
        else:
            i += 1
        i+=1
    return final
    """
    #Using in built python function.
    ans = []
    for i in nums:
        if nums.count(i) == 1:
            ans.append(i)
    return ans

print(singleNumber(nums = [1,2,1,3,2,5]))