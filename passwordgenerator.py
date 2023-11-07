import random
import string

def generate_password(length, min_letters, min_numbers, min_symbols):
    characters = ""

    if min_letters > 0:
        characters += string.ascii_letters
    if min_numbers > 0:
        characters += string.digits
    if min_symbols > 0:
        characters += string.punctuation

    if len(characters) == 0:
        print("Please select at least one character type.")
        return None

    password = ""

    if min_letters > 0:
        password += ''.join(random.choice(string.ascii_letters) for _ in range(min_letters))
    if min_numbers > 0:
        password += ''.join(random.choice(string.digits) for _ in range(min_numbers))
    if min_symbols > 0:
        password += ''.join(random.choice(string.punctuation) for _ in range(min_symbols))

    remaining_length = length - len(password)
    password += ''.join(random.choice(characters) for _ in range(remaining_length))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))
    min_letters = int(input("Enter the minimum number of letters: "))
    min_numbers = int(input("Enter the minimum number of numbers: "))
    min_symbols = int(input("Enter the minimum number of symbols: "))

    for _ in range(num_passwords):
        password = generate_password(length, min_letters, min_numbers, min_symbols)

        if password:
            print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
