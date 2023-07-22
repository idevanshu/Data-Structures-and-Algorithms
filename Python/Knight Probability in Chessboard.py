import numpy as np


def knightProbability(n, k, row, column):
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),(2, 1), (2, -1), (-2, 1), (-2, -1)]
    dp = np.zeros((n, n))
    dp[row][column] = 1

    for i in range(k):
        new = np.zeros((n, n))
        for r in range(n):
            for c in range(n):
                for dr, dc in moves:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < n and 0 <= new_c < n:
                        new[new_r][new_c] += dp[r][c] / 8
        dp = new

    probability = np.sum(dp)
    return probability

print(knightProbability(n=3, k=2, row=0, column=0))