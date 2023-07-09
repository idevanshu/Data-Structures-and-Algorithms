from collections import Counter
import itertools

def largestVariance(s):
    count = Counter(s)

    ans = 0

    for i,j in itertools.permutations(count,2):
        i_count = count[i]
        j_count = count[j]

        diff = 0

        seen_i = seen_j = False

        for char in s:
            if char not in (i,j):
                continue

            if diff < 0:
                if not i_count:
                    break

                if not j_count:
                    ans = max(ans,diff + i_count)
                    break
                
                seen_i = seen_j = False
                diff = 0

            if char == i:
                seen_i = True
                i_count -= 1
                diff += 1
            
            if char == j:
                seen_j = True
                j_count -= 1
                diff -= 1

            if seen_i and seen_j:
                ans = max(ans, diff)

    return ans

print(largestVariance("aababbb"))