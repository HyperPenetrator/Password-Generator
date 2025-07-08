import random
import string
import pyperclip

def generate_password(length=8, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print("Welcome to Simple Password Generator!")
length = int(input("Enter password length: "))
upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, upper, digits, symbols)
print("Generated password:", password)

pyperclip.copy(password)
print("Password copied to clipboard!")