def asteroidCollision(asteroids):
    ans = []
    for i in asteroids:
        while len(ans) and i < 0 and ans[-1] > 0:
            if ans[-1] + i == 0:
                ans.pop()
                break
            elif abs(i) < ans[-1]:
                break
            else:
                ans.pop()
                continue
        else:
            ans.append(i)
    return ans

print(asteroidCollision([5, 10, -5]))