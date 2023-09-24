import random
import string

word = "anant"

def Encrypt_message (word):
    random_chars = ''.join(random.choice(string.ascii_letters)for _ in range(3))
    word =  random_chars + word[1:] + word[0] + random_chars
    return word

def reverse(word):
    return word[1:] + word[0]


def code (word):
    if(len(word)>= 3):
         return Encrypt_message(word)
    else:
         return reverse(word)

input_from_user =input("Enter the secret message for ( ENCRYPTION ) : ")
Words_process = input_from_user.split()
Encoded_words = [code(word) for word in Words_process]
Encoded_sentece = ' '.join(Encoded_words)
print(f"your encoded statement is : {Encoded_sentece}")
