PASSWORD_LENGTH = 8


def main():
    password = get_password()
    print("Password:", len(password)*"*")


def get_password():
    prompt = str(input("Password: "))
    while len(prompt) < PASSWORD_LENGTH:
        print("At least 8 characters.")
        prompt = str(input("Password: "))
    else:
        return prompt


main()
