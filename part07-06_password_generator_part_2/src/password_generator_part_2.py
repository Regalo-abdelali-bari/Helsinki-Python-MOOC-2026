# Write your solution here
import random
import string
def generate_strong_password(n_l:int , num: bool , cha: bool):
    my_list1 = string.ascii_lowercase
    my_list2 = "!?=+-()#"
    my_list3 = string.octdigits
    sentence =  ""
    i = 1
    while len(sentence) < n_l:
        if num and i == 2:
            sentence += random.choice(my_list3)
            i += 1
        elif cha and i == 3:
            sentence += random.choice(my_list2)
            i = 1
        else:
            sentence += random.choice(my_list1)
            i += 1

    return sentence
        
        
if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, True, True))