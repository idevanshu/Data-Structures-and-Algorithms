import math
def minEatingSpeed(piles, h):
    left,right = 1, max(piles)
    res = right

    while left <= right:
        k = (left + right) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        
        if hours <= h:
            res = min(res,k)
            right = k - 1
        else:
            left = k + 1

    return res

print(minEatingSpeed(piles = [3,6,7,11], h = 8))