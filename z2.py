"""W alfabecie Morse’a litery i znaki przestankowe są zapisywane za pomocą ciągu kropek i kresek. W
poniższej tabeli znajduje się fragment tego alfabetu. Opracuj program, który poprosi użytkownika o
podanie ciągu tekstowego, a następnie zamieni go na ciąg tekstowy zapisany za pomocą alfabetu
Morse’a."""

MORSE_CODE = {
    ' ': ' ',
    ',': '.-.-.-',
    '.': '......',
    '?': '..--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
}

text = input('Text: ')
code = []
for letter in text:
    if letter in MORSE_CODE:
        encoded = MORSE_CODE[letter]
    else:
        continue
    code.append(encoded)

print('Code: ', ' '.join(code))
