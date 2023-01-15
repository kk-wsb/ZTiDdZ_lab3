import string
import random
import base64


def encodeb64(text):
    return base64.standard_b64encode(text.encode('ascii'))


def generatePassword():
    exclusion_dict = ['123', 'test', 'admin']  # Mozna by to zaciagnac z nltk ale nie pojdzie w online
    characters = string.digits + string.ascii_letters + string.punctuation

    while True:
        password = ''
        for i in range(random.randint(8, 64)):  # Maks dlugosc na 64, wiecej nie ma sensu imho
            password += random.choice(characters)
        if password not in exclusion_dict: return password


# Sprawdzenie
print("Your encoded text is:", encodeb64("Test kodowania base64"))
print("Your decoded string is:", base64.b64decode(encodeb64("Test kodowania base64")).decode('ascii'))
print("Your password is:", generatePassword())
