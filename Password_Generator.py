import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""
# Creating an empty string to store the password.
password = ''

for x in range(0, nr_letters):
    y = random.choice(letters)
    password += y

for x in range(0, nr_symbols):
    y = random.choice(symbols)
    password += y

for x in range(0, nr_numbers):
    password += random.choice(numbers)

"""

# Create an empty list to store the password.
password = []

for x in range(0, nr_letters):
    y = random.choice(letters)
    password.append(y)

for x in range(0, nr_symbols):
    y = random.choice(symbols)
    password.append(y)

for x in range(0, nr_numbers):
    y = random.choice(numbers)
    password.append(y)


rand_pass = ''.join(random.sample(password, len(password)))
print(rand_pass)