import string
import random
def generate_passwd(size):
    all_char=string.ascii_letters+string.digits+string.punctuation
    passwd=""
    for char in range(size):
        rand_char = random.choice(all_char)
        passwd=passwd+rand_char
    return passwd
passwd_len=int(input('Enter the no. of charcters in password: '))
new_password=generate_passwd(passwd_len)
print("your new password: ",new_password)
