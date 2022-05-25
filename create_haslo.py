import random

import login

def get_password():

    A_B_C = 'AaBbCcDdEeFfGgHhIiJiKkLlMmNnJjPpQqRrSsTtUuVvWwXxYyZz'
    NUMBERS = '0123456789'
    SYMBOLS = A_B_C + NUMBERS
    repeat = True
    password = ''
    while repeat:
        password = ''
        # password += A_B_C[random.randint(0, 51)]
        for _ in range(7):
            password += SYMBOLS[random.randint(0, 61)]

        # if login.valid_password(password):
        #     repeat = False
        # else:
        #     repeat = True

        repeat = login.valid_password(password)

    # Вернуть сгенерированный пароль.
    return password




