def get_login_name(first, last, idnumber):
    # Pobranie trzech pierwszych liter imienia
    set1 = first[0:3]
    # Pobranie trzech pierwszych liter nazwiska
    set2 = last[0:3]
    # Pobranie trzech ostatnich znaków numeru albumu
    set3 = idnumber[-3:]
    # Połączenie ze sobą zbiorów znaków
    login_name = set1 + set2 + set3
    # Zwrot nazwy użytkownika
    return login_name


# Funkcja valid_password() akceptuje argument
# w postaci hasła i zwraca wartość True lub False
def valid_password(password):
    is_digit = False
    is_lower = False
    is_upper = False


    for symbol in password:
        if symbol.isdigit():
            is_digit = True
        elif symbol.islower():
            is_lower = True
        elif symbol.isupper():
            is_upper = True

    is_not_valid = True
    if is_digit and is_lower and is_upper:
        is_not_valid = False

    return is_not_valid
