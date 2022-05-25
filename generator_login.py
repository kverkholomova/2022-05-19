"""Zadanie domowe 1.
Zmodyfikuj aplikację do generowania loginów i haseł w taki sposób, aby tworzony był plik z loginami
oraz hasłami (jawnymi). W dalszym etapie należałoby weryfikować loginy i hasła studentów na podsta-
wie informacji zawartych w tym pliku. Masz tutaj wolną rękę."""

import create_haslo
import login
import validate_login

dane = open("Info_student.txt", "r")
result = open("login.txt", "w")
haslo = open("haslo.txt", "w")


def main():
    for k in dane:
        dane_im = k.split()
        first = dane_im[0]
        last = dane_im[1]
        idnumber = dane_im[2]
        print('Twoja nazwa użytkownika to:')
        print(login.get_login_name(first, last, idnumber))
        # result.write("Login: ")
        result.write(login.get_login_name(first, last, idnumber))
        result.write("\n")
        # result.write("Haslo: ")
        haslo.write(create_haslo.get_password())
        haslo.write("\n")
        validate_login.login_val()


main()
