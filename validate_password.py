import login
def main():
 password = input('Podaj hasło: ')
 while not login.valid_password(password):
     print('Hasło jest nieprawidłowe.')
     password = input('Podaj hasło: ')
     print('Hasło jest prawidłowe.')
main()
