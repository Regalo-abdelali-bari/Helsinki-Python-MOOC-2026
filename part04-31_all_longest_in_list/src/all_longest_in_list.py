def all_the_longest(my_list:list):
    list_my=my_list.copy()
    longer = len(my_list[0])
    word = my_list[0]
    i = 0
    for item in list_my:
        
        if len(item) == longer:
            continue
        elif len(item) > longer:
            i = my_list.index(item)
            longer = len(item)
            word = item
            
            my_list = my_list[i:]
        elif longer > len(item):
            index = my_list.index(item)
            
            my_list.pop(index)
            
    
            
        

        
    return my_list