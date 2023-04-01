def combinationSum(candidates, target):
    numbers = []
    def recursion(i,c,sum):
        
        if sum == target:
            numbers.append(c.copy()) 
            return
        if i>= len(candidates) or sum>target:
            return
        
        c.append(candidates[i])
        recursion(i,c,sum + candidates[i])
        c.pop()
        recursion(i + 1,c,sum)
    recursion(0,[],0)
    return numbers


print(combinationSum(candidates = [2,3,6,7], target = 7))