# Write your solution here
def everything_reversed(my_list: list):
    
    list_my=[]
    for item in my_list:
        list_my.append(item[::-1])
        
    return list_my[::-1]



