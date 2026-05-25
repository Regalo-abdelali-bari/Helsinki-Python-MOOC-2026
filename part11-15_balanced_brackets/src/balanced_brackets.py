
def balanced_brackets(my_string: str):
    
    my_string = "".join(cha for cha in my_string if cha in "([])")
    if len(my_string) == 0:
        return True
    if my_string[0] in "()":
        if not (my_string[0] == '(' and my_string[-1] == ')') :
            return False
    elif my_string[0] in "[]":
        if not (my_string[0] == '[' and my_string[-1] == ']') :
            return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])