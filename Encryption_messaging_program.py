# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string
# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode
import random

def reverse (word):
    rev_word = word[::-1]
    return word
def code (word):
    if(len(word)<= 3):
        reverse(word)
        return word
    else:
        first_letter = word[0]
        word = word[1:]+first_letter
        
