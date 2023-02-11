import string 

def isPalindrome(s):
    p = string.punctuation
    arr = []
    x = s.lower().replace(" ","")
    for i in x:
        if i in p:
            x = x.replace(i,"")
    arr.append(x)
    result = "".join(arr)
    if result == result[::-1]:
        return True
    else: 
        return False

while True:
    s = str(input("Enter the string: "))
    print(isPalindrome(s))