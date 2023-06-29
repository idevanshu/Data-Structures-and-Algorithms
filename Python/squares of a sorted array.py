def sortedSquares(nums):
    square = [i*i for i in nums]
    square.sort()
    return square

print(sortedSquares([-7,-3,2,3,11]))