def minimizeMax(nums, p):
    nums.sort()
    N = len(nums)

    left, right = 0, max(nums)

    def check(n):
        count = 0
        i = 0

        while i + 1 < N:
            if nums[i + 1] - nums[i] <= n:
                i += 2
                count += 1
            else:
                i += 1
            if count >= p:
                return True
        return count >= p

    while left < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


print(minimizeMax(nums=[10, 1, 2, 7, 1, 3], p=2))