def longestValidParentheses(s):
    stack = [-1]
    mx = 0
    for x,y in enumerate(s):
        if y == "(":
            stack.append(x)
        else:
            stack.pop()
            if not stack:
                stack.append(x)
            else:
                mx = max(mx,x-stack[-1])
    return mx

print(longestValidParentheses("(()"))

