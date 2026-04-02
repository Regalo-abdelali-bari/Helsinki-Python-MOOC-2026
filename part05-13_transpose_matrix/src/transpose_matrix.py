# Write your solution here
def transpose(matrix: list):
    copy_list=[]
    i = 0
    while i < len(matrix):
        copy_list.append([])
        i += 1
    i = 0
    for items in matrix:
        for item in items:
            copy_list[i].append(item)
            i += 1
        i = 0
    while i <len(matrix):
        matrix[i] = copy_list[i]
        i += 1

if __name__ == "__main__":
    matrix = [[2, 3, 4, 5], [6, 7, 8, 9], [9, 8, 7, 6], [5, 4, 3, 2]]
    transpose(matrix)
    print(matrix)

