def ces(shift, file, alphabet, alphabet_inverse):
    with open(file) as f, open('output.txt', 'w') as out:
        message = f.read()
        for let in message:
            if let.lower() in alphabet:
                pos = alphabet[let.lower()]
                ans = alphabet_inverse[(pos - shift) % 26].upper()
                out.write(ans)
            else:
                out.write(let)

def vig(key_word, file, alphabet, alphabet_inverse):
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