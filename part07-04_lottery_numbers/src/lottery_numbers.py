
from random import *
def lottery_numbers(amount: int, lower: int, upper: int):
    my_list = []
    while len(my_list) <= amount - 1:
        num = randint(lower, upper)
        if num not in my_list :
            my_list.append(num)
    my_list.sort()
    
    return my_list
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)