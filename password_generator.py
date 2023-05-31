import random
import string


low_characters = list(string.ascii_lowercase)
up_characters = list(string.ascii_uppercase)
special_characters = list(string.punctuation)

characters = list(low_characters + up_characters + special_characters)

lenght = int(input('Password lenght: '))



def pass_generating(lenght):
    i = 0
    heslo = ''
    while i < lenght:
        random_character = characters[random.randint(0, len(characters) - 1)]
        heslo += random_character
        
        i += 1
    return heslo

password = pass_generating(lenght)

print(password)