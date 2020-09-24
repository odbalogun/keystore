import os

KEYSTORE = 'keystore.txt'


def line_break():
    print("-"*30)


def display_key_pairs():
    ensure_keystore_exists()
    keystore_lines = open(KEYSTORE, 'r')

    for line in keystore_lines.readlines():
        print(line)
    keystore_lines.close()
    line_break()


def ensure_keystore_exists():
    if os.path.isfile(KEYSTORE):
        return
    open(KEYSTORE, 'a').close()


def add_key_pair(key, value):
    ensure_keystore_exists()
    # todo check that key does not already exist
    try:
        with open(KEYSTORE, 'a') as keystore_file:
            keystore_file.write(f"{key.upper()}: {value}")
            keystore_file.write("\n")
    except IOError:
        print(f"Could not write to {KEYSTORE}. Ensure file is writable")
        print("Exiting.....")
        exit()
    print("Success. Keystore has been updated")


print("Welcome to the Key Store")
line_break()
input_options = [1, 2, 3, 4]
loop = True
while loop:
    print("What would you like to do?")
    print("1 - Add new key pair")
    print("2 - Display all key pairs")
    print("3 - Search key pairs")
    print("4 - Quit")

    try:
        selection = int(input())
    except ValueError:
        print("Invalid input... Enter an integer")
    else:
        if selection == 4:
            print("Exiting.....")
            exit()

        if selection not in input_options:
            print("Invalid input... Select from the available options")

        if selection == 1:
            key = input("Enter your key: ")
            value = input("Enter its corresponding value: ")
            # save key pair
            add_key_pair(key, value)
        elif selection == 2:
            display_key_pairs()
        elif selection == 3:
            needle = input("Enter the key you want to retrieve: ")
