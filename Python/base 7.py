def convertToBase7(num):

    if num == 0:
        return "0"
    
    result = ""
    is_negative = False
    
    if num < 0:
        is_negative = True
        num = -num
    
    while num > 0:
        result = str(num % 7) + result
        num //= 7
        
    if is_negative:
        result = "-" + result
        
    return result



while True:
    x = int(input("Enter the number: "))
    print(convertToBase7(x))