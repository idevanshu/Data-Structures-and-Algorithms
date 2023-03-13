def merge(nums1,m,nums2,n):  
    last = m + n - 1

    for i in range(last, -1, -1):
        if n <= 0:
            break
        if m > 0 and nums1[m - 1] > nums2[n - 1]:
            nums1[i] = nums1[m - 1]
            m -= 1
        else:
            nums1[i] = nums2[n - 1]
            n -= 1
    
    return nums1



print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))