from PIL import Image
from colorama import init, Fore

init()

while True:
    filter = input('Choose filter [a, li, lu]')
    if filter == 'a' or filter == 'li' or filter == 'lu':
        break
    else:
        print('Please choose a valid filter')

while True:
    invert = input('Invert brightness? [y,n]')
    if invert == 'y' or invert == 'n':
        break
    else:
        print('Please input y or n')

def RGB_to_bright(t):
    if filter == 'a':
        return sum(t) / 3
    elif filter == 'li':
        return (max(t) + min(t)) / 2
    elif filter == 'lu':
        return t[0] * 0.21 + t[1] * 0.72 + t[2] * 0.07

img = Image.open('pikachu.jpg')
resized = img.resize((200, 150))
img_data = list(resized.getdata())
data = [img_data[x:x + resized.width] for x in range(0, len(img_data), resized.width)]
bright_data = []
for x in range(len(data)):
    bright_data.append(list(map(RGB_to_bright, data[x])))
if invert == 'y':
    for x in range(len(bright_data)):
        for y in range(len(bright_data[x])):
            bright_data[x][y] = 255 - bright_data[x][y]
#65 Chars in ascii 255 puntos de brightness nos da un ratio de 3,92 bright por char
# brightness de 177 dividido 3.92 nos da 45.15, o sea el caracter 45
def bright_to_ascii(n):
    ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    ratio = round(n / 3.92)
    if ratio == 0:
        return ascii[ratio]
    else:
        return ascii[ratio - 1]

ascii_data = []
for x in range(len(bright_data)):
    ascii_data.append(list(map(bright_to_ascii, bright_data[x])))
clean_data = []
for x in ascii_data:
    clean_data.append(''.join(x))
art = '\n'.join(clean_data)
print(Fore.GREEN + art)
