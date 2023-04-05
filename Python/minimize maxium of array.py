def minimizeArrayValue(nums):
    n = len(nums)
    nums.reverse()
    l,r = 0,  10 ** 9

    def good(target):
        carry =  0
        for x in nums:
            x += carry
            carry = 0
            if x >= target:
                carry = x - target
        return carry == 0
    
    while l < r:
        mid = (l+r)//2
        if good(mid):
            r = mid
        else:
            l = mid + 1
    return l

print(minimizeArrayValue([3,7,1,6]))