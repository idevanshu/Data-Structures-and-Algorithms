def isSubsequence(s, t):
    count = 0
    for i in t:
        if count == len(s):
            break
        if s[count] == i:
            count += 1
    return count == len(s)
print(isSubsequence("ab","baab"))