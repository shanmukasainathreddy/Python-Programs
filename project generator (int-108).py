import random
import string

def password_generator(length):
    # list of all the characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # generate a random password
    password = "".join(random.choice(characters) for i in range(length))
    # check if the password is strong
    if check_password(password):
        return password
    else:
        return password_generator(length)
    
def check_password(password):
    # check if the password is strong
    if (any(char.islower() for char in password) and
        any(char.isupper() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)):
        return True
    else:
        return False
    
# main function
if _name_ == "_main_":
    length = int(input("Enter the length of the password: "))
    print(password_generator(length))
