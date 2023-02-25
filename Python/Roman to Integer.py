
def romanToInt(string_roman):
    Symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    total = 0
    prev_value = 0
    for i in string_roman[::-1]:
        curr_Value = Symbol[i]
        if prev_value > curr_Value:
            total -= curr_Value
        else:
            total += curr_Value
        prev_value = curr_Value
 
    return total

while True:
    roman = str(input("Enter the roman number: ")).upper()

    print(romanToInt(roman))


