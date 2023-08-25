# ask user
# ask for pass length
# gen password
import random
import string
import pyperclip

characters = list(string.ascii_letters + string.digits + "!@#$%&*")

def generate_password():
    password_length = int(input("How long would you like your password to be?"))
    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("Your password is: "+password)
    return password
def copy_password(password):
    pyperclip.copy(password)
    copied = pyperclip.paste()
    return copied

print("Would you like to generate password?" )
choice = input("Yes/No: ")
if choice == "Yes":
    generated_password = generate_password()
    copy = input("Copy to clipboard? Yes/No ")
    if copy == "Yes":
        copy_password(generated_password)
        print("Copied to clipboard.")
else:
    print("Program will shut down...")
    exit()






