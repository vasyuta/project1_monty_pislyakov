from random import randint
import webbrowser
import shifr
import deshifr
import hack
import globals
import steg

def choos_ces_mode(file):
    print('Выберите режим: шифровка, дешифровка, взлом')
    do = input()
    if do == 'взлом':
        hack.ces(file, globals.alphabet, globals.alphabet_inverse)
    else:
        print('Введите сдвиг')
        shift = int(input())
        if do == 'шифровка':
            shifr.ces(shift, file, globals.alphabet, globals.alphabet_inverse)
        else:
            deshifr.ces(shift, file, globals.alphabet, globals.alphabet_inverse)

def choose_vig_mode(file):
    print('Выберите режим: шифровка, дешифровка')
    do = input()
    print('Введите ключ')
    key = input()
    if do == 'шифровка':
        shifr.ver(key, file, globals.alphabet, globals.alphabet_inverse)
    else:
        deshifr.vig(key, file, globals.alphabet, globals.alphabet_inverse)

def choose_ver_mode(file):
    print('Выберите режим: шифровка, дешифровка')
    do = input()
    if do == 'шифровка':
        shifr.ver(file, globals.alphabet, globals.alphabet_inverse)
    else:
        print('Введите ключ')
        key = input()
        deshifr.vig(key, file, globals.alphabet, globals.alphabet_inverse)

def choose_steg_mode(file):
    print('Введите путь к фото')
    photo = input()
    print('Шифр или дешифровка')
    do = input()
    if do == 'дешифовка':
        steg.deshifr(photo)
    else:
        steg.shifr(file, photo)
        

def mem_joke():
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
    elif finale == 'my fingers are fast':
        print('Вам правда интересно? :) История про розыгрыши физтехами своих сокамерников. Спросите меня в тг или вживую!')

def choose_mode():
    print('Введите путь без кавычек (проверьте раскладку -- клавиша C коварна!)')
    file = input()
    print('Выберите режим: шифр Цезаря, шифр Виженера, шифр Вернама')
    rezhim = input()
    if rezhim == 'шифр Цезаря':
        choos_ces_mode(file)
    elif rezhim == 'шифр Виженера':
        choose_vig_mode(file)
    elif rezhim == 'шифр Вернама':
        choose_ver_mode(file)
    elif rezhim == 'Стеганография':
        choose_steg_mode(file)
    mem_joke()
    

choose_mode()
