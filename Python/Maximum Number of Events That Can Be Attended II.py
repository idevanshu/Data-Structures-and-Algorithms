def maxValue(events, k):
    events.sort(key=lambda x: x[1])
    dp = [[0] * (k + 1) for i in range(len(events) + 1)]

    for i in range(1, len(events) + 1):
        start, end, value = events[i - 1]
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
            low, high = 0, i - 1
            while low <= high:
                mid = (low + high) // 2
                if events[mid][1] < start:
                    low = mid + 1
                else:
                    high = mid - 1

            if low >= 0:
                dp[i][j] = max(dp[i][j], dp[low][j - 1] + value)

    return dp[-1][-1]


print(maxValue(events=[[1, 2, 4], [3, 4, 3], [2, 3, 1]], k=2))
