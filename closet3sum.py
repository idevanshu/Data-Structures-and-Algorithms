def threeSumClosest(nums,target):
    nums.sort()
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return current_sum
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum
    
nums =[1,1,1,0]
print(threeSumClosest(nums,-100))
