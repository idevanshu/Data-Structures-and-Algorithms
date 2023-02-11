def wordPattern(pattern, s):
    s = s.split()
    if len(pattern) != len(s):
        return False
    
    right_left = {}
    left_right = {}

    for r, l in zip(pattern, s):
        if r not in right_left:
            right_left[r] = l
        if l not in left_right:
            left_right[l] = r
        if right_left[r] != l or left_right[l] != r:
            return False
        
    return True

pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern,s))