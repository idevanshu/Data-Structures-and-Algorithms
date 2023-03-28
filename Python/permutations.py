from itertools import permutations
def permute(nums):
    data = []
    per = permutations(nums)
    for i in per:
        data.append(list(i))
    return data
print(permute(nums=[1,2,3]))