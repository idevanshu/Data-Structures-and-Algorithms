def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    print(nums1)
    if n % 2 == 0:
        median = (nums1[int(n/2)-1] + nums1[int(n/2)])/2
    else:
        median = float(nums1[int(n/2)])
    
    return median

nums1 = [1,2]
nums2 = [3]

print(findMedianSortedArrays(nums1=nums1,nums2=nums2))