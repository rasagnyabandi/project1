import string
import random
def generate_passwd(size):
    all_char=string.digits+string.ascii_letters+string.punctuation
    password = ""
    password +=random.choice(string.ascii_uppercase)
    password +=random.choice(string.ascii_lowercase)
    password +=random.choice(string.digits)
    password +=random.choice(string.punctuation)
    for char in range(size-4):

        password+=random.choice(all_char)

    return password
paswd_len = int(input("enter the no. of charcters: "))
new_password=generate_passwd(paswd_len)
print(new_password)
