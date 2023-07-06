def runningSum(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        calc = result[i - 1] + nums[i]
        result.append(calc)

    return result


print(runningSum([1, 2, 3, 4]))
