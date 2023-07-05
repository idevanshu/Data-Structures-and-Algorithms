def longestSubarray(nums):
    length = 0
    l, r = 0, 0
    n = len(nums)
    count = 0

    while r < n:
        if nums[r] == 0:
            count += 1
        while count > 1:
            if nums[l] == 0:
                count -= 1
            l += 1
        r += 1
        length = max(length, r - l - 1)

    return length


print(longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1]))
print(longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(longestSubarray([1, 1, 1]))
