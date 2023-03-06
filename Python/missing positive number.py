def findKthPositive(arr,k):
    skiped = []
    for i in range(1,arr[len(arr)-1]):
        if i not in arr:
            skiped.append(i)

    count = len(skiped)
    if count < k:
        return arr[-1] + (k-count)
    else:
        return skiped[k-1]


print(findKthPositive(arr = [1,2,3], k = 5))