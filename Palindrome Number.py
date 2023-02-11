
def isPalindrome(x):
    orginal = str(x)
    revser =str(x)[::-1]
    print(f"{orginal} : {revser}")
    
    if orginal == revser:
        return True
    else:
        return False

while True:
    n = int(input("Enter the number: "))
    print(isPalindrome(n))