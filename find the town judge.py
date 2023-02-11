def findJudge(n,trust):
    if n == 1 and not trust:
        return -1
    
    check = [0] * n
    for i,j in trust:
        if i<=n and i>0 and j <=n and j > 0:
            check[i-1] -= 1
            check[j-1] += 1
    for i in range(n):
        if check[i] == n-1:
            return i +1
    return -1


print(findJudge(4,[[1,3],[1,4],[2,3],[2,4],[4,3]]))