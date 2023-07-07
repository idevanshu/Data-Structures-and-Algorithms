def maxConsecutiveAnswers(answerkey,k):
    #Sliding Window
    max_count = 0
    max_consecutive = 0
    From = 0
    count = {'T': 0, 'F': 0}

    for i in range(len(answerkey)):
        count[answerkey[i]] += 1
        max_count = max(max_count, count['T'],count['F'])

        if (i - From + 1) - max(max_count, count['T'], count['F']) > k:
            count[answerkey[From]] -= 1
            From += 1
    max_consecutive = max(max_consecutive, len(answerkey) - From)
    return max_consecutive

print(maxConsecutiveAnswers("TTFF", 2))