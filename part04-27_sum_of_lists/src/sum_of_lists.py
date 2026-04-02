# Write your solution here
def list_sum(items1: list, items2: list):
    my_list = []
    n = 0
    for i in items1:
        items2[n] += i
        n += 1
    return items2

