import itertools

def canConstruct(ransomNote, magazine):
    first = list(ransomNote)
    second = list(magazine)
    count = 0
    for i in first:
        if i in second:
            second.remove(i)
            count += 1

    if len(first) == count:
        return True
    return False      

print(canConstruct(ransomNote = "a", magazine = "b"))

print(canConstruct(ransomNote = "aa", magazine = "aab"))