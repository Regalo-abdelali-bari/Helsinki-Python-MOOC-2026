# Write your solution here
from fractions import *
def fractionate(amount: int):
    my_list = []
    for i in range(amount):
        my_list.append(Fraction(1,amount))
    return my_list

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))

