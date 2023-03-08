def maxNumber(nums1,nums2,k):
    def get_max_subsequence(nums, k):
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and len(stack) + n - i > k and nums[i] > stack[-1]:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        return stack
    
    m, n = len(nums1), len(nums2)
    res = [0] * k
    i = max(0, k - n)
    j = min(k, m)
    while i <= j:
        subseq1 = get_max_subsequence(nums1, i)
        subseq2 = get_max_subsequence(nums2, k - i)
        combined = [max(subseq1, subseq2).pop(0) for _ in range(k)]
        res = max(res, combined)
        i += 1
        j = min(j, k - i + m)
    return res


print(maxNumber(nums1 = [6,7], nums2 = [6,0,4], k = 5))
print("\n")
print(maxNumber(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5))