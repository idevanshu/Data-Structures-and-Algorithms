def maximumProduct(nums):
    nums.sort()  # Sort the numbers in ascending order
    n = len(nums)
    # There are two possible cases to consider:
    # 1. The maximum product is the product of the three largest positive numbers
    # 2. The maximum product is the product of the two smallest negative numbers and the largest positive number
    return max(nums[n-1] * nums[n-2] * nums[n-3], nums[0] * nums[1] * nums[n-1])

print(maximumProduct([-100, -98, -1, 2, 3, 4]))
print(maximumProduct([-1, -2, -3]))
print(maximumProduct([-1000, -1000, 1000]))
