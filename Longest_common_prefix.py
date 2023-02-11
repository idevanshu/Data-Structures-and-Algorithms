

def longestCommonPrefix(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    prefix = []
    for chars in zip(*strs):
        print(chars)
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return "".join(prefix)
        

strs = ["flower","flow","fl"]

print(longestCommonPrefix(strs))