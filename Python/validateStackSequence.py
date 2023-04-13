def validate(pushed, popped):
    n = len(popped)
    stack = []
    i = 0
    for x in pushed:
        stack.append(x)
        while stack and i<n and stack[-1]==popped[i]:
            i+=1
            stack.pop()
    return stack==[]

print(validate(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]))