# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    i = 0
    for row in my_matrix:
        for item in row:
            if element == item:
                i += 1
    return i