# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1 
    if maximum % 2 != 0:
        maximum -= 1 
    while beginning <= maximum:
        yield beginning
        beginning += 2

