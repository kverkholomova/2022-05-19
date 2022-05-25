
def login_val():
    with open("Info_student.txt", "r") as in_, open("login.txt", "r") as res_:
        inputs = in_.readlines()
        inputs = [i.strip() for i in inputs]

        results = res_.readlines()
        results = [i.strip() for i in results]

        logins = results[::2]
        print(logins)

        if len(inputs) != len(logins):
            print("Count of results is not equal to count of data")

        for i in range(len(inputs)):
            info = inputs[i]
            name, surname, code = info.split()
            login = logins[i]
            expected = name[:3] + surname[:3] + code[-3:]
            is_valid = expected == login
            print(f"{info=} {login=} {is_valid=}")



login_val()
