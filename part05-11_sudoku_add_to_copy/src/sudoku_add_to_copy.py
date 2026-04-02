# Write your solution here
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    my_copy = []
    my_copy2 = []
    for items in sudoku:
        for item in items:
            my_copy2.append(item)
        my_copy.append(my_copy2)
        my_copy2=[]
    my_copy[row_no][column_no] = number
    return my_copy


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
    

