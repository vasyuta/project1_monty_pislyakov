from random import randint

def ces(shift, file, alphabet, alphabet_inverse):
    if not isinstance(shift, int):
      print('Введите ключ-число')
      return
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        for let in message:
            if let.lower() in alphabet:
                pos = alphabet[let.lower()]
                ans = alphabet_inverse[(shift + pos) % 26].upper()
                out.write(ans)
            else:
                out.write(let)

def vig(key_word, file, alphabet, alphabet_inverse):
    if not isinstance(shift, int):
        print('Введите ключ-слово')
      return
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

def ver(file, alphabet, alphabet_inverse):
    key_word = ''
    with open(file) as text:
        message = text.read()
        letter_amount = 0
        for x in message:
            if x.lower() in alphabet:
                letter_amount += 1
    for i in range(letter_amount):
        key_word += alphabet_inverse[randint(0, 26)]
    vig(key_word, file)
    print('Ключ: ', key_word)
