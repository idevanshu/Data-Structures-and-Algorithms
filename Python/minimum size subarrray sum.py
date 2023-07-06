def  minSubArrayLen(target,nums):
    # Sliding Window
    left = 0
    total = 0
    final = len(nums)+1

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            final = min(final,right - left + 1)
            total -= nums[left]
            left += 1    

    return 0 if final == len(nums)+1 else final

print(minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))