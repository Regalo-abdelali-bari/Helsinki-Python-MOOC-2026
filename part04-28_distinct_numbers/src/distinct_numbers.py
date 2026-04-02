# Write your solution here
def distinct_numbers(items: list):
    my_list = []
    for i in items:
        if not i in my_list:
            my_list.append(i)
    return sorted(my_list)