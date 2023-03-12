def sortPeople(names,heights):
    x = sorted(zip(names,heights), key=lambda x: x[1], reverse=True)
    return list(i for i,y in x)

print(sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))