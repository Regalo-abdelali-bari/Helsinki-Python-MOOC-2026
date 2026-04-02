# Write your solution here
def shortest(my_list:list):
    short = len(my_list[0])
    short1 = my_list[0]
    for item in my_list:
        if len(item) < short  > 1:
            short = len(item)
            short1 = item
    return short1