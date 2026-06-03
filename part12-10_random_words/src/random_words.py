# Write your solution here:
from random import shuffle
def word_generator(characters: str, length: int, amount: int):
    char = list(characters)
    for i in range(amount):
        yield "".join(cha for cha in char[:length])
        shuffle(char)


    
