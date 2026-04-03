# write your solution here

def matrix_sum():
    with open("matrix.txt") as matrix:
        i = 0
        for items in matrix:
            items = items.replace(","," ").split()
            for item in items:
                item = int(item)
                i += item
        return i

def matrix_max():
    with open("matrix.txt") as matrix:
        i = 0
        for items in matrix:
            items = items.replace(","," ").split()
            for item in items:
                item = int(item)
                if item > i:
                    i = item
        return i
    
def row_sums():
    with open("matrix.txt") as matrix:
        i = 0
        my_list= []
        for items in matrix:
            items = items.replace(","," ").split()
            for item in items:
                item = int(item)
                i += item
            my_list.append(i)
            i = 0   
        return my_list
if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())