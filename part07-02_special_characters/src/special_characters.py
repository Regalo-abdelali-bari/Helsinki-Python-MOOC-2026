# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    letter1 = ""
    letter2 = ""
    letter3 = ""
    for cha in my_string:
        if cha in ascii_letters:
            letter1 += cha
        elif cha in punctuation:
            letter2 += cha
        else:
            letter3 += cha
    return letter1 , letter2 , letter3

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])