def buddyStrings(s, goal):
    if len(s) != len(goal):return False
    if s == goal and len(set(s)) < len(s):return True

    differences = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            differences.append([s[i],goal[i]])

    if len(differences) == 2 and differences[0] == differences[-1][::-1]:
        return True
    
    return False


print(buddyStrings("ab","ab")) #False
