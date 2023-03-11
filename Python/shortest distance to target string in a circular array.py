def closetTarget(words,target, startIndex):
    n = len(words)
    got_it = float('inf')
    for i in range(n):
        if words[i] == target:
            distance = min(abs(i - startIndex), n - abs(i - startIndex))
            if distance < got_it:
                got_it = distance
    if got_it == float('inf'):
        return -1
    return got_it

print(closetTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1))