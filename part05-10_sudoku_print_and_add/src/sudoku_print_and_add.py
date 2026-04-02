# Write your solution here
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number
    return sudoku
def print_sudoku(sudoku: list):
    i = 0
    j = 0
    for row in sudoku:
        j += 1
        for item in row:
            i += 1
            if i % 3== 0 and item != 0:
                print(f"{item}  ",end="")
            elif i % 3== 0 :
                print("_  ",end="")
            elif item == 0:
                print("_ ",end="")
            else:
                print(f"{item} ",end="")
                
        if j % 3==0:
            print()
        print()
    
