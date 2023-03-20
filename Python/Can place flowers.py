def canPlaceFlowers(flowerbed,n):
    f = [0] + flowerbed + [0]

    for i in range(1,len(f)-1):
        if f[i -1] == 0 and f[i] == 0 and f[i+1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0

    #Another way
    """
    emp = 0 if flowerbed[0] else 1
        for f in flowerbed:
            if f:
                n -= int((emp - 1)/2)
                emp = 0
            else:
                emp += 1
        n -= (emp)//2
        return n<=0
    """


print(canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2))