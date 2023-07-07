def smallerNumbersThanCurrent(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        ans = 0
        while count  < len(nums):
            if nums[i] > nums[count]:
                ans += 1
                count += 1
            else:
                count += 1
        result.append(ans)
    
    return result

print(smallerNumbersThanCurrent([8,1,2,2,3]))