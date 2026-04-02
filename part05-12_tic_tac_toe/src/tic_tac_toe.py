# Write your solution here
# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if y > 2 or x > 2 or  game_board[y][x] != "" :
        return False
    game_board[y][x] = piece
    print(game_board)
    return True

if __name__ == "__main__":
    
    print(play_turn([['O', '', 'O'], ['O', 'X', 'O'], ['', 'O', '']], 2, -1, "X"))
    
