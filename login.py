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
    # Przypisanie wartości False zmiennym boolowskim
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    # Rozpoczęcie weryfikacji hasła. Na początku
    # sprawdzana jest jego długość
    if len(password) > 7:
        correct_length = True
    # Trzeba sprawdzić każdy znak
    # i przypisać odpowiednią wartość
    # po znalezieniu wymaganego znaku
    for ch in password:
        if ch.isupper():
            has_uppercase = True
    if ch.islower():
        has_lowercase = True
    if ch.isdigit():
        has_digit = True
    # Ustalenie, czy wszystkie wymagania zostały spełnione
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False
    # Zwrot zmiennej is_valid
    return is_valid
