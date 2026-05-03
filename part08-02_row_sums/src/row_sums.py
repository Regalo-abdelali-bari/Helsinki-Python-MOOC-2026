# Write your solution here
def row_sums(my_matrix: list):
    for matrix in my_matrix:
        sum_matrix = sum(matrix)
        matrix.append(sum_matrix)

