import PIL
import numpy as np
import itertools


def shifr(txt_path, img_path):
    with open(txt_path, 'r') as text:
        message = text.read() + '&'
    b = ''
    for symb in message:
        b += format(ord(symb), '08b')
    message = b
    with PIL.Image.open(img_path) as img:
        inf = np.array(img)
        idx = 0
        for i, j, k in itertools.product(range(img.size[1]), range(img.size[0]), range(2)):
            inf[i][j][k] = int(bin(inf[i][j][k])[2:][: 8] + message[idx], 2)
            idx += 1
            if idx == len(message):
                break
        Image.fromarray(inf).save('ПРАЙВАТ.png')


def deshifr(img_path):
    message = ''
    with PIL.Image.open(img_path) as img:
        inf = np.array(img)
        with open('output.txt', 'w') as vyhlop:
            current = ''
            curr_idx = 0
            for i, j, k in itertools.product(range(img.size[1]), range(img.size[0]), range(3)):
                current += bin(inf[i][j][k])[-1]
                idx += 1
                if curr_idx == 32:
                    symb = chr(int(current, 2))
                    if symb == '&':
                        vyhlop.write(message)
                        return
                    message += symb
                    current = ''
                    idx = 0
