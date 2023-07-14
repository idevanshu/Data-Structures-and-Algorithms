def longestSubsequence(arr, difference):
    ans = 0
    values_diff = {}

    for i in arr:
        count = 1
        if i - difference in values_diff:
            count += values_diff[i - difference]
        values_diff[i] = count
        ans = max(ans, values_diff[i])

    return ans


print(longestSubsequence(arr=[1, 2, 3, 4], difference=1))
