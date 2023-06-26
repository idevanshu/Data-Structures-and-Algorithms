def toHex(num):
    if num == 0:
        return "0"
    hexadecimal = hex(num & 0xFFFFFFFF)
    hexadecimal_digits = hexadecimal[2:]
    return hexadecimal_digits

print(toHex(-1))