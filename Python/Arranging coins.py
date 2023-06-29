def arrangeCoins(n):
    left, right = 1, n

    while left <= right:
        mid = left + (right - left) // 2
        curr = mid * (mid + 1) // 2

        if curr == n:
            return mid

        if curr < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

print(arrangeCoins(100))