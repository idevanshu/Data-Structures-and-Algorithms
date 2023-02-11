def isValid(s):
    par = []
    for i in s:
        if i in "([{":
            par.append(i)
        elif i in ")]}":
            if not par:
                return False
            if i == ")" and par[-1] != "(":
                return False
            if i == "]" and par[-1] != "[":
                return False
            if i == "}" and par[-1] != "{":
                return False
            par.pop()
    return not par

while True:
    st = str(input("Enter parentheses: "))
    print(isValid(st))