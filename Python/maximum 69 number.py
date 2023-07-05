def maximum69Number(num):
    digits = str(num)
    for i in range(len(digits)):
        if digits[i] == "6":
            digits = digits[:i] + "9" + digits[i+1:]
            break #Changing first occurence of 6 only.
    return int(digits)
            
print(maximum69Number(9669))