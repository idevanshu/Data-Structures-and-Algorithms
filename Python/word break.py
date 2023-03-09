def wordBreak(s,wordDict):
    n = len(s)
    dp = [False] * (n+1)
    dp[len(s)] = True

    for i in range(n-1,-1,-1):
        for j in wordDict:
            if (i + len(j)) <= n and s[i:i+len(j)] == j:
                dp[i] = dp[i + len(j)]
            if dp[i] == True:
                break

    return dp[0]

print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(wordBreak("bb",["a","b","bbb","bbbb"]))