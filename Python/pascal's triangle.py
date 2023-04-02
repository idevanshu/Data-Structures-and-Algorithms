def generate(numRows):
    result = [[1]]
    #building rows
    for i in range(numRows -1):
        base_structure = [0] + result[-1] + [0]
        row = []
        #Columns
        for j in range(len(result[-1]) + 1):
            row.append(base_structure[j] + base_structure[j+1])
        result.append(row)
    return result
    
while True:
    x = int(input("Enter a Number: "))
    print(generate(x))
