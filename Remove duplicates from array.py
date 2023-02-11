def removeDuplicates(nums):
    first = set(nums)
    second = list(first)

    return [set(len(second)+1)]


print(removeDuplicates([1,1,2]))