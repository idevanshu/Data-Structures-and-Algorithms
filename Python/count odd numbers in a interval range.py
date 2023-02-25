def countOdds(low, high):
    return (high - low) // 2 + (low % 2 != 0 or high % 2 != 0)

print(countOdds(3,7))