def soupServings(n):
    def dfs(a, b):
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1.0
        if b <= 0:
            return 0.0
        if cache[a][b] > 0:
            return cache[a][b]

        cache[a][b] = 0.25 * (dfs(a - 4, b) +
                              dfs(a - 3, b - 1) +
                              dfs(a - 2, b - 2) +
                              dfs(a - 1, b - 3))
        return cache[a][b]

    cache = [[0.0] * 192 for i in range(192)]
    return 1 if n >= 4800 else dfs((n + 24) // 25, (n + 24) // 25)


print(soupServings(50))
