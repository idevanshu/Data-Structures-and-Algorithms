def lengthOfLongestSubstring(s):
        check = []
        count = 0
        length = 0
        for i in range(len(s)):
            if s[i] in check:
                length = max(length, len(check))
                while s[count] != s[i]:
                    check.remove(s[count])
                    count += 1
                count += 1
            else:
                check.append(s[i])
        length = max(length, len(check))
        return length

###Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
print(lengthOfLongestSubstring("pwwkew"))