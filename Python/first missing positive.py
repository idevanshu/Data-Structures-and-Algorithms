def firstMissingPositive(nums):
    nums.sort()
    compare = [i for i in nums]
    ret = 0
    for i in range(1,len(nums)+1):
        if i not in compare:
            ret += i
            break
        else:
            continue
    
    if ret == 0:
        ret += nums[len(nums)-1] + 1
    
    return ret

print(firstMissingPositive([3,4,-1,1]))