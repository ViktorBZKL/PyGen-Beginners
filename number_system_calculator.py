def bin_to_dec(binary):
    return int(binary, 2)

def oct_to_dec(octal):
    return int(octal, 8)

def hex_to_dec(hexadecimal):
    return int(hexadecimal, 16)

def dec_to_bin(decimal):
    return bin(decimal)[2:]

def dec_to_oct(decimal):
    return oct(decimal)[2:]

def dec_to_hex(decimal):
    return hex(decimal)[2:]

def convert_number(number, from_base, to_base):
    if from_base == 1:
        decimal = bin_to_dec(number)
    elif from_base == 2:
        decimal = oct_to_dec(number)
    elif from_base == 3:
        decimal = hex_to_dec(number)
    else:
        decimal = int(number)

    if to_base == 1:
        result = dec_to_bin(decimal)
    elif to_base == 2:
        result = dec_to_oct(decimal)
    elif to_base == 3:
        result = dec_to_hex(decimal)
    else:
        result = str(decimal)

    return result

print("Выберите начальную систему счисления:")
print("1. Двоичная")
print("2. Восьмеричная")
print("3. Шестнадцатеричная")
print("4. Десятичная")

from_base = int(input("Введите номер системы счисления: "))

number = input("Введите число: ")

print("Выберите конечную систему счисления:")
print("1. Двоичная")
print("2. Восьмеричная")
print("3. Шестнадцатеричная")
print("4. Десятичная")

to_base = int(input("Введите номер системы счисления: "))

result = convert_number(number, from_base, to_base)

print(f"Результат: {result}")
