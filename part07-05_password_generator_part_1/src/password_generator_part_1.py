# Write your solution here
from random import sample
def generate_password(n_l:int):
    my_list = alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
    sentence = ""
    for cha in sample(my_list,n_l):
        sentence += cha
    return sentence
if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))