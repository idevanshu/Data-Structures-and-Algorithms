def addToArrayForm(num,k):
    stack = []
    carry = 0
    i = len(num) - 1

    while i >= 0 or k > 0:
        if i >= 0:
            digit_sum = num[i] + k % 10 + carry
            i -= 1
        else:
            digit_sum = k % 10 + carry

        stack.append(digit_sum % 10)
        carry = digit_sum // 10
        k //= 10

    if carry:
        stack.append(carry)

    return stack[::-1]

print(addToArrayForm(num = [1,2,0,0], k = 34))