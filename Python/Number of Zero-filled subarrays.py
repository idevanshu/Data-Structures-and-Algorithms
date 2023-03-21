import itertools
from scipy.special import comb

def zeroFilledSubarray(nums):
    count = 0
    for key,group in itertools.groupby(nums):
        """
        when, nums = [1,3,0,0,2,0,0,4])
        print(list(group))
        [1]
        [3]
        [0, 0]
        [2]
        [0, 0]
        [4]
        """
        c = len(list(group))

        if key == 0:
            # from scipy.special import comb
            """
            comb help in calculating number of ways to choose k items from
            a set of n items without replacement and without regard to order.
            """
            count += comb(c+1,2)

    return int(count)

    #Mathematical approach
    """
    n = len(nums)
    num = 0
    count = 0

    for i in range(n):
        if(nums[i]==0):
            count += 1
        else:
            # n x (n+1)/2 
            num +=(count*(count+1)/2)
            count = 0
    
    if count != 0 :
        num +=(count*(count+1)/2)

    return int(num)
    """

print(zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))