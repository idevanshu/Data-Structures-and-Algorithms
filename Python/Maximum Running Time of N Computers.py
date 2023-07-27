def max_running_time(n, batteries):
    left, right = 1 , sum(batteries) // n
    
    def check(target):
        count = 0
        for i in batteries:
            count += min(target, i)
        return count >= n * target
    
    while left < right:
        mid = (left + right + 1) // 2
        
        if check(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

print(max_running_time(n = 2, batteries = [3,3,3]))