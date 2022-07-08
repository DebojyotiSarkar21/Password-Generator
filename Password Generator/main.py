#Password Generator Project


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Choice = input("'Easy' or 'Hard' or 'Both' ?\n").lower()

if Choice == "easy":
    password1 = ""
    for char in range(1, nr_letters + 1):
        password1 += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password1 += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password1 += random.choice(numbers)
    print(f"Your Easy password is {password1}")

elif Choice == "hard":
    password_list = []
    for char in range(1, nr_letters + 1):
        password_list += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)
    random.shuffle(password_list)        #Shuffle the elements of the list
    password3 = ""                        #empty string to print the list as a string
    for char in password_list:
        password3 += char
    print(f"Your Hard Password can be {password3}")

elif Choice == "both":
    password = ""
    for char in range(1, nr_letters + 1):
        password += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password += random.choice(numbers)
    print(f"Easy - {password}")

    password_list1 = []
    for char in range(1, nr_letters + 1):
        password_list1 += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password_list1 += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password_list1 += random.choice(numbers)
    random.shuffle(password_list1)  # Shuffle the elements of the list
    password = ""  # empty string to print the list as a string
    for char in password_list1:
        password += char
    print(f"Hard - {password}")

else:
    print("PLEASE ENTER:    EASY / HARD / BOTH      ONLY")

