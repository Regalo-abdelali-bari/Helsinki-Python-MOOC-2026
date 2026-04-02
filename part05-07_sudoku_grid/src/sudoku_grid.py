# Write your solution here
#this function it gives True or False iranzantale
def row_correct(sudoku: list):
    items = []
    for row in sudoku:
        for item in row :
            if item in items and item != 0:
                return False
            items.append(item)
        items = []
    return True 


def column_correct(sudoku: list):
    items = []
    i = 0
    while i <= 8:
        for row in sudoku:
            if row[i] != 0 and row[i] in items:
                return False
            items.append(row[i])
        i += 1
        items =[]
    return True

# Write your solution here
#this function it gives True or False iranzantale
def block_correct(sudoku: list):
    items = []
    items1 = []
    i = 0
    index1 = 0
    index2 = 0
    while index1 <= 6 and index2 <= 6:
        while True:
            if len(items) == 9:
                break
            if i == 3:
                index1 += 1
                i = 0
            num = sudoku[index1][index2 + i]
            items.append(num)
            i += 1
        for item in items:
            if item != 0 and item in items1:
                return False
            items1.append(item)
        
        if index2 == 6 and index1 < 3:
            index2 = 0
            index1 = 3
        elif index2 == 6 and index1 < 6:
            index2 = 0
            index1 = 6
            
            
        else:
            index2 += 3
        if index1 < 3:
            index1 = 0
        elif index1 < 6:
            index1 = 3
        else: 
            index1 = 6
        
        i = 0
        items =[]
        items1=[]
    return True



def sudoku_grid_correct(sudoku: list):
    return row_correct(sudoku) and column_correct(sudoku) and block_correct(sudoku)











 






  









