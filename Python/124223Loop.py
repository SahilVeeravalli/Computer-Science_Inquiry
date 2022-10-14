#convert number to binary, octal, and hexadecimal
def bin(decimal):
    if(decimal > 0):
        bin((int)(decimal/2))
        print(decimal%2, end='')
        
decimal = int(input("Enter a decimal number: "))
bin(decimal)

def Oct(decimal):
    if(decimal > 0):
        Oct((int)(decimal/8))
        print(decimal%8, end='')
        
decimal = int(input("Enter a decimal number: "))
print("Octal: ", end='')
Oct(decimal)


def hex(dec_value):
    ret_val = str()
    while dec_value > 0:
        hex_value=dec_value%16
        dec_value=dec_value//16
        ret_val = char(hex_value) + ret_val
    return ret_val

def char(dec_digit):
    if dec_digit < 10:
        return str(dec_digit)
    if dec_digit == 10:
        return "A"
    if dec_digit == 11:
        return "B"
    if dec_digit == 12:
        return "C"
    if dec_digit == 13:
        return "D"
    if dec_digit == 14:
        return "E"
    if dec_digit == 15:
        return "F"
    
dec = int(input("Enter decimal value: "))
print(dec,"is equal to",hex(dec), "in hexadecimal")
