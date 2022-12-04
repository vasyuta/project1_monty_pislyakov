from random import randint
import webbrowser
import shifr
import deshifr
import hack

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
        hack.ces(file, alphabet, alphabet_inverse)
    else:
        print('Введите сдвиг')
        shift = int(input())
        if do == 'шифровка':
            shifr.ces(shift, file, alphabet, alphabet_inverse)
        else:
            deshifr.ces(shift, file, alphabet, alphabet_inverse)

if rezhim == 'шифр Виженера':
    print('Выберите режим: шифровка, дешифровка')
    do = input()
    print('Введите ключ')
    key = input()
    if do == 'шифровка':
        shifr.ver(key, file, alphabet, alphabet_inverse)
    else:
        deshifr.vig(key, file, alphabet, alphabet_inverse)

if rezhim == 'шифр Вернама':
    print('Выберите режим: шифровка, дешифровка')
    do = input()
    if do == 'шифровка':
        shifr.ver(file, alphabet, alphabet_inverse)
    else:
        print('Введите ключ')
        key = input()
        deshifr.vig(key, file, alphabet, alphabet_inverse)

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
