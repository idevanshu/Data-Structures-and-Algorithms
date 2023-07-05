def countConsistentStrings(allowed, words):
    count = 0
    for i in words:
        have = True
        for j in i:
            if j not in allowed:
                have = False
                break
        if have:
            count += 1
    return count

print(countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))