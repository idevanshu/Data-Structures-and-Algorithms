def combine(n,k):
    if k <= 0 or n <= 0:
        return []
    
    if k == 1:
        return [[i] for i in range(1, n+1)]

    return [j + [i] for i in range(k, n+1) for j in combine(i-1,k-1)]

print(combine(n = 4, k = 2))