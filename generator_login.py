"""Zadanie domowe 1.
Zmodyfikuj aplikację do generowania loginów i haseł w taki sposób, aby tworzony był plik z loginami
oraz hasłami (jawnymi). W dalszym etapie należałoby weryfikować loginy i hasła studentów na podsta-
wie informacji zawartych w tym pliku. Masz tutaj wolną rękę."""

import login
def main():
 first = input('Podaj imię: ')
 last = input('Podaj nazwisko: ')
 idnumber = input('Podaj numer albumu: ')
 print('Twoja nazwa użytkownika to:')
 print(login.get_login_name(first, last, idnumber))
main()
