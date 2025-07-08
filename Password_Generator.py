import random
import string

from password_generator import generate_password
def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    chars = list(string.ascii_lowercase)
    if use_upper:
        chars += list(string.ascii_uppercase)
    if use_digits:
        chars += list(string.digits)
    if use_symbols:
        chars += list("!@#$%^&*()-_=+[]{}|;:,.<>?/~`")
    if not chars:
        raise ValueError("No character sets selected!")
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_upper = input("Use uppercase letters? (y/n): ").lower().startswith("y")
    use_digits = input("Use digits? (y/n): ").lower().startswith("y")
    use_symbols = input("Use symbols? (y/n): ").lower().startswith("y")
    print(generate_password(length, use_upper, use_digits, use_symbols)
