def findTheDifference(s,t):
    main = list(s)
    for i in t:
        if i in main:
            main.remove(i)
        else:
            return i


print(findTheDifference("abcd","abcde"))