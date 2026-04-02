# Write your solution here
def who_won(game_board: list):
    i_1 = 0
    i_2 = 0
    for row in game_board:
        for element in row:
            if element == 1:
                i_1 += 1
            elif element == 2:
                i_2 += 1
    if i_1 > i_2 :
        return 1
    elif i_1 < i_2 :
        return 2
    return 0
if __name__ == "__main__":
    print(who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]]))