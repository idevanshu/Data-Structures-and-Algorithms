def minSpeedOnTime(dist, hour):
    left = 1
    right = 10 ** 8

    def check(speed):
        current = 0
        for i in dist[:-1]:
            current += (i + speed  - 1) // speed
        return current + (float(dist[-1]) / float(speed)) <= hour

    while left < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid + 1

    if left >= 10 ** 8:
        return -1
    return left

print(minSpeedOnTime(dist = [1,3,2], hour = 6))