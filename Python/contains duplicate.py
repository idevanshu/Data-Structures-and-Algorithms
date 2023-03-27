def containsDuplicate(nums):
    data = set()
    for n in nums:
        if n in data:
            return True
        data.add(n)
    return False

print(containsDuplicate(nums = [1,2,3,1]))