def majorityElement(nums):
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
        if count[i] > len(nums)//2:
            return i

print(majorityElement([2,2,1,1,1,2,2]))
