import string
import itertools   
def letterCombinations(digits):
    if not digits:
        return []
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = [""]
    for digit in digits:
        temp = []
        for c in mapping[digit]:
            for item in res:
                temp.append(item + c)
        res = temp
    return res
    

print(letterCombinations("9999"))