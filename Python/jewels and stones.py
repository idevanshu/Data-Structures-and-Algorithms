def numJewelsInStones(jewels,stones):
    #Simple 
    """
    count = 0 
    for i in stones:
        if i in jewels:
            count += 1
    return count 
    """
    #Simple One-liner
    """
    count = sum(1 for i in stones if i in jewels)
    return count
    """
    #using Lamda
    count = sum(map(lambda i: i in jewels, stones))
    return count

print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))