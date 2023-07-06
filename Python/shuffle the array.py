def shuffle(nums,n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans

print(shuffle(nums = [2,5,1,3,4,7], n = 3))