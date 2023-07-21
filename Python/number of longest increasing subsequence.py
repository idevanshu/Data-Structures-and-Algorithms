def findNumberOfLIS(nums):
    n = len(nums)
    if n <= 1:return n
    length = [1] * n
    count = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if length[j] + 1 > length[i]:
                    length[i] = length[j] + 1
                    count[i] = count[j]
                elif length[j] + 1 == length[i]:
                    count[i] += count[j]

    max_length = max(length)
    counts = sum(count[i] for i in range(n) if length[i] == max_length)
    return counts

print(findNumberOfLIS([1, 3, 5, 4, 7]))