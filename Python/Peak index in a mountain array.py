import numpy as np
def peakIndexInMountainArray(arr):
    #Normal Binary Search approach.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left
    """

    # Using numpy for binary search.
    arr = np.array(arr)
    ans = np.argmax(arr)
    return ans

print(peakIndexInMountainArray([0,1,0]))