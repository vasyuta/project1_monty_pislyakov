import deshifr

def ces(file, alphabet, alphabet_inverse):
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
    deshifr.ces(shift, file, alphabet, alphabet_inverse)
