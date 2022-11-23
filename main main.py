
from random import randint
import webbrowser

def ces_shifr(shift, file, alphabet, alphabet_inverse):
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        for let in message:
            if let.lower() in alphabet:
                pos = alphabet[let.lower()]
                ans = alphabet_inverse[(shift + pos) % 26].upper()
                out.write(ans)
            else:
                out.write(let)

def ces_deshifr(shift, file, alphabet, alphabet_inverse):
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        for let in message:
            if let.lower() in alphabet:
                pos = alphabet[let.lower()]
                ans = alphabet_inverse[(pos - shift) % 26].upper()
                out.write(ans)
            else:
                out.write(let)

def ces_hack(file, alphabet, alphabet_inverse):
    freq = {}
    for i in alphabet:
        freq[i] = 0
    with open(file) as text:
        message = text.read()
        for let in message:
            if let.lower() in alphabet:
                freq[let.lower()] += 1
    max_kolvo = -1
    letter_max = ''
    for letter in freq:
        if freq[letter] > max_kolvo:
            letter_max = letter
            max_kolvo = freq[letter]
    pos_letter_max = alphabet[letter_max]
    shift = (pos_letter_max - 4) % 26
    ces_deshifr(shift, file)

def vig_deshifr(key_word, file, alphabet, alphabet_inverse):
    key_word = key_word.lower()
    length = len(key_word)
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        letter_amount = 0
        for x in message:
            if x.lower() in alphabet:
                letter_amount += 1
        for i in range(len(key_word), letter_amount):
            key_word += key_word[i % length]
        i = 0
        for let in message:
            if let in alphabet:
                pos_key = alphabet[key_word[i]]
                pos_let = alphabet[let.lower()]
                ans = alphabet_inverse[(pos_let - pos_key) % 26].upper()
                out.write(ans)
            else:
                out.write(let)
            i += 1

def vig_shifr(key_word, file, alphabet, alphabet_inverse):
    key_word = key_word.lower()
    length = len(key_word)
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        letter_amount = 0
        for x in message:
            if x.lower() in alphabet:
                letter_amount += 1
        for i in range(len(key_word), letter_amount):
            key_word += key_word[i % length]
        i = 0
        for let in message:
            if let in alphabet:
                pos_key = alphabet[key_word[i]]
                pos_let = alphabet[let.lower()]
                ans = alphabet_inverse[(pos_key + pos_let) % 26].upper()
                out.write(ans)
            else:
                out.write(let)
            i += 1



def ver_shifr(file, alphabet, alphabet_inverse):
    key_word = ''
    with open(file) as text:
        message = text.read()
        letter_amount = 0
        for x in message:
            if x.lower() in alphabet:
                letter_amount += 1
    for i in range(letter_amount):
        key_word += alphabet_inverse[randint(0, 26)]
    vig_shifr(key_word, file)
    print('Ключ: ', key_word)


def main():
    print('Введите путь без кавычек (проверьте раскладку -- клавиша C коварна!)')
    file = input()

    print('Выберите режим: шифр Цезаря, шифр Виженера, шифр Вернама')
    alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
            'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
            'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    alphabet_inverse = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                    11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                    21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}


    rezhim = input()
    if rezhim == 'шифр Цезаря':
        print('Выберите режим: шифровка, дешифровка, взлом')
        do = input()
        if do == 'взлом':
            ces_hack(file, alphabet, alphabet_inverse)
        else:
            print('Введите сдвиг')
            shift = int(input())
            if do == 'шифровка':
                ces_shifr(shift, file, alphabet, alphabet_inverse)
            else:
                ces_deshifr(shift, file, alphabet, alphabet_inverse)

    if rezhim == 'шифр Виженера':
        print('Выберите режим: шифровка, дешифровка')
        do = input()
        print('Введите ключ')
        key = input()
        if do == 'шифровка':
            vig_shifr(key, file, alphabet, alphabet_inverse)
        else:
            vig_deshifr(key, file, alphabet, alphabet_inverse)

    if rezhim == 'шифр Вернама':
        print('Выберите режим: шифровка, дешифровка')
        do = input()
        if do == 'шифровка':
            ver_shifr(file, alphabet, alphabet_inverse)
        else:
            print('Введите ключ')
            key = input()
            vig_deshifr(key, file, alphabet, alphabet_inverse)

    print('Если хотите узнать о нас больше, то введите "i wanna believe"; если хотите узнать смешную историю, то введите "my fingers are fast"')

    finale = input()
    if finale == 'i wanna believe':
       print('Понравилась работа? Поставите оценку? :3')
       print('Мы в социальных сетях:')
       print('Telegram: @vasiliipl')
       print('ВКонтаке: https://vk.com/vasilipl')
       print('Instagram: продукт компании "Meta", признанной экстремистской и запрещённой на территории РФ')
       print('Творчество моего дедушки: https://stihi.ru/avtor/pislyakov?ysclid=lau2c7jnpm732116318 (стих про Байдена -- бомба)')
       print('Творчество моего папы: https://scholar.google.com/citations?user=d7rCieAAAAAJ')
       print('ГЛАВНОЕ: https://profi.ru/profile/PislyakovVV/?ysclid=las8yy18co150067651\n(ПОДНЯЛИ ЦЕНЫ В ОКТЯБРЕ! СЛЕДУЮЩЕЕ ПОВЫШЕНИЕ В ДЕКАБРЕ)')
       print('В А Ж Н О:   С К И Д К И   Н А   Т Е О Р М Е Х   В   Я Н В А Р Е !!!')
       webbrowser.open('https://stihi.ru/avtor/pislyakov?ysclid=lau2c7jnpm732116318', new=1)
       webbrowser.open('https://profi.ru/profile/PislyakovVV/?ysclid=las8yy18co150067651', new=1)
       webbrowser.open('https://profi.ru/repetitor/?seamless=1&tabName=ORDER&chosenProfileId=PislyakovVV#slideId=103339', new=1)

    if finale == 'my fingers are fast':
        print('Вам правда интересно? :) История про розыгрыши физтехами своих сокамерников. Спросите меня в тг или вживую!')

main()