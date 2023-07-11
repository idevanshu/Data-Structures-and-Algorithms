def generateParenthesis(n):
    stack = []
    ans = []

    def backTrack(left, right):
        if left == right == n:
            ans.append("".join(stack))
            return

        if left < n:
            stack.append("(")
            backTrack(left + 1, right)
            stack.pop()

        if right < left:
            stack.append(")")
            backTrack(left, right + 1)
            stack.pop()

    backTrack(0, 0)
    return ans


print(generateParenthesis(3))
