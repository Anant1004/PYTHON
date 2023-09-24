import random
import string

def Encrypt_message (word):
    random_chars = ''.join(random.choice(string.ascii_letters)for _ in range(3))
    word =  random_chars + word[1:] + word[0] + random_chars
    return word

def reverse_encrypt(word):
    return word[1:] + word[0]


def code (word):
    if(len(word)>= 3):
        return Encrypt_message(word)
    else:
        return reverse_encrypt(word)


def Decrypt_message(word):
    decrypted_word = word[3:-3] 
    last_letter = word[-1] + decrypted_word
    return last_letter

def reverse_decrypt(word):
    return word[::-1]

def decode(word):
    if len(word) < 3:
        return reverse_decrypt(word)
    else:
        return Decrypt_message(word)

msg = int(input("Enter 0 for ENCRYPTION //// Enter 1 for DECRYPTION \n"))
if (msg == 0):
    input_from_user = input("Enter the secret message for ( ENCRYPTION ) : ")
    Words_process = input_from_user.split()
    Encoded_words = [code(word) for word in Words_process]
    Encoded_sentece = ' '.join(Encoded_words)
    print(f"ENCODED STATEMENT IS --->: {Encoded_sentece}")
if(msg == 1):
    input_from_user = input("Enter the secret message for ( DECRYPTION ) : ")
    Words_process = input_from_user.split()
    Decoded_words = [decode(word) for word in Words_process]
    Decoded_sentence = ' '.join(Decoded_words)
    print(f"Your decoded statement is: {Decoded_sentence}")

