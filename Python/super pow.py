def superPow(a,b):
    mod = 1337
    return pow(a, int("".join(map(str, b))), mod)

print(superPow(2,[1,0]))