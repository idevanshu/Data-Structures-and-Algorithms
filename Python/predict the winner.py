def PredictTheWinner(nums):
    n = len(nums)

    def check(left,right):
        if left == right:
            return nums[left] 

        leftScore = nums[left] - check(left + 1, right)
        rightScore = nums[right] - check(left, right-1)

        return max(leftScore, rightScore)

    if check(0, n -1) >= 0:
        return True
    return False

print(PredictTheWinner(nums = [1,5,2]))
print(PredictTheWinner(nums = [1,5,233,7]))