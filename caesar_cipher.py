eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def code(text, n):
    result = ''

    for i in text:
        if i in rus_lower_alphabet:
            letter = (rus_lower_alphabet.index(i) + 1 + n) % 32
            result += rus_lower_alphabet[letter - 1]
        elif i in rus_upper_alphabet:
            letter = (rus_upper_alphabet.index(i) + 1 + n) % 32
            result += rus_upper_alphabet[letter - 1]
        elif i in eng_lower_alphabet:
            letter = (eng_lower_alphabet.index(i) + 1 + n) % 26
            result += eng_lower_alphabet[letter - 1]
        elif i in eng_upper_alphabet:
            letter = (eng_upper_alphabet.index(i) + 1 + n) % 26
            result += eng_upper_alphabet[letter - 1]
        else:
            result += i
    
    print(result)

def decode(text, n=0):
    if n == 0 and (text[0] in rus_lower_alphabet or text[0] in rus_upper_alphabet):
        n = 32
    elif n == 0 and (text[0] in eng_lower_alphabet or text[0] in eng_upper_alphabet):
        n = 26
    else:
        result = '' 
        for i in text:
            if i in rus_lower_alphabet:
                letter = (rus_lower_alphabet.index(i) + 1 - n) % 32
                result += rus_lower_alphabet[letter - 1]
            elif i in rus_upper_alphabet:
                letter = (rus_upper_alphabet.index(i) + 1 - n) % 32
                result += rus_upper_alphabet[letter - 1]
            elif i in eng_lower_alphabet:
                letter = (eng_lower_alphabet.index(i) + 1 - n) % 26
                result += eng_lower_alphabet[letter - 1]
            elif i in eng_upper_alphabet:
                letter = (eng_upper_alphabet.index(i) + 1 - n) % 26
                result += eng_upper_alphabet[letter - 1]
            else:
                result += i
        print(result)
        return
    
    for i in range(n):
        result = '' 
        for j in text:
            if j in rus_lower_alphabet:
                letter = (rus_lower_alphabet.index(j) + 1 - i) % 32
                result += rus_lower_alphabet[letter - 1]
            elif j in rus_upper_alphabet:
                letter = (rus_upper_alphabet.index(j) + 1 - i) % 32
                result += rus_upper_alphabet[letter - 1]
            elif j in eng_lower_alphabet:
                letter = (eng_lower_alphabet.index(j) + 1 - i) % 26
                result += eng_lower_alphabet[letter - 1]
            elif j in eng_upper_alphabet:
                letter = (eng_upper_alphabet.index(j) + 1 - i) % 26
                result += eng_upper_alphabet[letter - 1]
            else:
                result += j
        print(result)


choice = input('Вы хотите шифровать текст или дешифровать? (ш = шифровать, д = дешифровать) ')

if choice == 'ш':
    text = input('Введите текст для шифрования: ')
    n = int(input('Введите ключ от шифра: '))
    code(text, n)
elif choice == 'д':
    text = input('Введите текст для дешифрования: ')
    is_n = input('Вы знаете ключ от шифра? (д = да, н = нет) ')
    if is_n.lower() == 'д':
        n = int(input('Введите ключ от шифра: '))
        decode(text, n)
    else:
        decode(text)