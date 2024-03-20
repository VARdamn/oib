'''
Шифрование посимвольно: crypted[i] = text[i] XOR key[i]
Обратно аналогично: text[i] = crypted[i] XOR key[i]
Для того, чтобы определить ключ: key[i] = crypted[i] XOR text[i]
'''
import random


def int2hex(n: int):
    return hex(n)[2:].upper()


def validate(hex_arr: list):
    '''
    Добавляет ведущий ноль к каждому символу, в котором не 2 байта
    '''
    new_arr = []
    for el in hex_arr:
        new_arr.append(f'0{el}') if len(el) == 1 else new_arr.append(el)
    return new_arr


def generate_key(length: int):
    '''
    Генерация рандомного ключа длины length
    '''
    return validate([int2hex(random.randint(0, 255)) for _ in range(length)])


def encrypt(text: str, key: list = None):
    '''
    Выводит шифротекст для заданного текста.
    Если ключа нет, то генерируется случайный ключ
    '''

    text_16 = [char.encode(encoding='cp1251').hex().upper() for char in text]
    if not key:
        key = generate_key(length=len(text))

    print(f"Ключ шифрования:", ' '.join(str(s) for s in key))
    print(f"Исходный текст:", ' '.join(text_16))
    encrypted_text = []
    for i in range(len(text)):
        xor_char = int(text_16[i], 16) ^ int(key[i], 16)
        encrypted_text.append(int2hex(xor_char))

    encrypted_text = validate(encrypted_text)
    ciphertext = bytes.fromhex(''.join(encrypted_text)).decode('cp1251')
    print(f'Шифротекст: {ciphertext}\n\n')

    return {
        'key': key,
        'ciphertext': ciphertext
    }


def decrypt(ciphertext: str, key: list = None):
    ''''''
    ciphertext_16 = [char.encode('cp1251').hex().upper() for char in ciphertext]
    if not key:
        key = generate_key(length=len(ciphertext))

    print(f"Ключ шифрования:", ' '.join(str(s) for s in key))
    print(f"Исходный шифротекст:", ciphertext)

    decrypted_text = []
    for i in range(len(ciphertext)):
        xor_char = int(ciphertext_16[i], 16) ^ int(key[i], 16)
        decrypted_text.append(int2hex(xor_char))

    decrypted_text = validate(decrypted_text)
    decrypted_text = bytes.fromhex(''.join(decrypted_text)).decode('cp1251')
    print('Расшифрованный текст: ', decrypted_text)
    return {
        'key': key,
        'text': decrypted_text
    }


def find_key(text):
    '''
    Подбирает ключ, с помощью которого сообщение было зашифровано
    '''
    decrypted_text = ''
    encryption = encrypt(text)
    while decrypted_text != text:
        decryption = decrypt(encryption['ciphertext'])
        decrypted_text = decryption['text']
        print(f'Полученный текст: {decrypted_text}')
    print(f"Ключ успешно подобран! {decryption['key']}")


encryption = encrypt('С Новым Годом, друзья!')
decrypt(encryption['ciphertext'])