# Write your solution here
def row_correct(sudoku: list, row_no: int):
    items = []
    for row in sudoku[row_no]:
        if row != 0 and row  in items:
            return False
        items.append(row)
    return True
 


        