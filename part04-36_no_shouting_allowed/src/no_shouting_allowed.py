# Write your solution here
def no_shouting(my_list: list):
    list_my=[]
    for item in my_list:
        if item.isupper():
            continue
        list_my.append(item)
    return list_my