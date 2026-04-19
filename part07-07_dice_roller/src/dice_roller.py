# Write your solution here
import random
def roll(die: str):
    d = {"A" : [3, 3, 3, 3, 3, 6],
         "B" : [2, 2, 2, 5, 5, 5],
         "C" : [1, 4, 4, 4, 4, 4]
         }
    return random.choice(d[die])

def play(die1: str, die2: str, times: int):
    won1 = 0
    won2 = 0
    tie = 0
    while True:
        player1 = roll(die1)
        player2 = roll(die2)
        if player1 > player2:
            won1 += 1
        elif player2 > player1:
            won2 += 1
        else:
            tie += 1
        if won1 + won2 + tie == times:
            break
    return won1 , won2 , tie



if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)