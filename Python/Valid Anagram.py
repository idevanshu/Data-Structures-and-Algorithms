from collections import Counter
def isAnagram(s,t):
    return Counter(s) == Counter(t)


print(isAnagram(s = "anagram", t = "nagaram"))