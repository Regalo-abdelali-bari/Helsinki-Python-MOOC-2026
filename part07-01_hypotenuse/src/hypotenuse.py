# Write your solution here
from math import sqrt
def hypotenuse(leg1: float, leg2: float) :
    result = leg1 ** 2 + leg2 ** 2
    return sqrt(result)

if __name__ == "__main__":
    print(hypotenuse(1,2)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951