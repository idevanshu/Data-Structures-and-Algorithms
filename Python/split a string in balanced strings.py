def balancedStringSplit(s):
    count = 0
    l,r= 0,0

    for i in s:
        if i == "L":
            l += 1
        elif i == "R":
            r += 1
        
        if l == r:
            count += 1
            l += 1
            r += 1
    
    return count

print(balancedStringSplit("RLRRLLRLRL"))