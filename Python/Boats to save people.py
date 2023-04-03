def numRescueBoats(people,limit):
    people.sort()

    boats = 0
    l,r=0,len(people)-1
    while l<=r:
        remaining = limit - people[r]
        r -= 1
        boats += 1
        if l <=r and remaining >= people[l]:
            l += 1
    return boats


print(numRescueBoats([3,2,2,1], limit = 3))