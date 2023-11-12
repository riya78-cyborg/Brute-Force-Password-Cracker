import string
import random

def crack_password(password):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
        attempts += 1
        # print(f'attempts {attempts} : {guess}')
        if password == guess:
            return attempts

password = input("Enter pasword to be guessed: ")

print("Cracking the password...")

attempts = crack_password(password)

print(f"The password was cracked in {attempts} attempts")