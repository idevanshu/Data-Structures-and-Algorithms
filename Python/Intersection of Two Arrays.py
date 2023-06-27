def intersection(nums1,nums2):
        final = set()
        for i in nums1:
            if i in nums2:
                final.add(i)
        return list(final)


print(intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))