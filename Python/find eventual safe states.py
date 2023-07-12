def eventualSafeNodes(graph):
    n = len(graph)
    hashmap = {}
    ans = []

    def dfs(node):
        if node in hashmap:return hashmap[node]
        hashmap[node] = False
        for i in graph[node]:
            if not dfs(i):
                return False
        hashmap[node] = True
        return True
    
    for i in range(n):
        if dfs(i):
            ans.append(i)

    return ans


print(eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
