# Write your solution here
import random
def words(n: int, beginning: str):
    my_list = []
    with open("words.txt") as my_file:
        for word in my_file:
            word = word.strip()
            if word.startswith(beginning) :
                my_list.append(word)

    if len(my_list2) < n:
        raise ValueError
        
    return random.sample(my_list,n)
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)
