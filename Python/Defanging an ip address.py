def defanIPaddr(address):
    ans = ""
    for i in address:
        if i == ".":
            ans += "[.]"
        else:
            ans += i
    return ans

print(defanIPaddr("1.1.1.1"))