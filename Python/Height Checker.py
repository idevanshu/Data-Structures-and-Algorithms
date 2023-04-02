def heightChecker(heights):
    count = sum(x != y for x,y in zip(heights,sorted(heights)))
    return count


    #Detailed appraoch
    # sort_heights = sorted(heights)
    # count = 0
    # for i in range(len(heights)):
    #     if heights[i] != sort_heights[i]:
    #         count += 1
    #     else:
    #         continue
    # return count

print(heightChecker([1,1,4,2,1,3]))


