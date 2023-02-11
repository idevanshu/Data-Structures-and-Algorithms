

def intToRoman(num):
    roman_numbers = {1000: 'M',900: 'CM',500: 'D',400: 'CD',100: 'C',90: 'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V', 4: 'IV',1: 'I'}

    '''
    Logic 
    We should break the number in sum of 
    1000,500,100,50,10,5,1 
    '''

    result = ''
    for value, symbol in roman_numbers.items():
        while num >= value:
            result += symbol
            num -= value
    return result

while True:
    number = int(input("Enter the number: "))
    print(intToRoman(number))