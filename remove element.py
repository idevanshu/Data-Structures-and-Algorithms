def removeElement(nums,val):
    new_list = []
    for i in nums:
        if i != val:
            new_list.append(i)
    return int(len(new_list))



nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums,val))