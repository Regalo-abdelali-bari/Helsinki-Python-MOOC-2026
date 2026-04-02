# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    items = []
    items1 = []
    i = 0
    
    while True:
        if len(items) == 9:
            break
        if i == 3:
            row_no += 1
            i = 0
        num = sudoku[row_no][column_no + i]
        items.append(num)
        i += 1
    for item in items:
        if item != 0 and item in items1:
            return False
        items1.append(item)
    return True


        
        
        
