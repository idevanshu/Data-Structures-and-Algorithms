def singleNumber(nums):
    new = []
    remove = []
    final = []
    for i in nums:
        if i not in new:
            new.append(i)
        else:
            remove.append(i)

    for i in new:
        if i not in remove:
            final.append(i)
    
    for i in final:
        return int(i)
print(singleNumber([2,2,1]))