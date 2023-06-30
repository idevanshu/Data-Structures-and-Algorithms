def repeatedSubstringPattern(s):
    temp = ""
    len_s = len(s)
    for i in range(len_s // 2):
        temp += s[i]
        if len_s % len(temp) == 0:
            if temp * (len_s // len(temp)) == s:
                return True
    return False

print(repeatedSubstringPattern("aaabaaab"))