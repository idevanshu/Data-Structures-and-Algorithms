def canFinish(numCourses,prerequisites):
    maping = {i:[] for i in range(numCourses)}

    for i,j in prerequisites:
        maping[i].append(j)

    visited = set()

    def dfs(i):
        if i in visited:return False
        if maping[i] == []:return True

        visited.add(i)
        for j in maping[i]:
            if not dfs(j):return False
        visited.remove(i)
        maping[i] = []
        return True
    
    for i in range(numCourses):
        if not dfs(i): return False
    return True

print(canFinish(numCourses = 2, prerequisites = [[1,0]]))