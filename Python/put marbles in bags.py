def putMarbles(weights, k):
    w = []

    for x, y in zip(weights, weights[1:]):
        w.append(x + y)
    w.sort()
    n = len(w)

    mini = weights[0] + weights[-1]
    maxi = weights[0] + weights[-1]
    for i in range(k - 1):
        mini += w[i]
        maxi += w[n-i-1]

    return maxi - mini


print(putMarbles([1, 3, 5, 1], 2))
