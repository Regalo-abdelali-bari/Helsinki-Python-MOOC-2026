# Write your solution here
def even_numbers(items: list):
    my_list = []
    for i in items:
        if i % 2 == 0:
            my_list.append(i)
    return my_list