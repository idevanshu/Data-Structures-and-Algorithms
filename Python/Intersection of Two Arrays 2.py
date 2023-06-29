def intersect(nums1, nums2):
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans

print(intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))