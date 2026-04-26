# Write your solution here
#step 1:import the libery string wich take functions (string.ascii_letters , string.digits )
#Part 1:creat a function his name "change_case(orig_string: str)" wich take one argement 
    #step 1:use a for loop to change a cha
    #step 2:check if cha is lower_case change in uppercase or reverse and append in the list "sentence"
    #step 3:return the sentence
#Part 2:creat a function his name "split_in_half(orig_string: str)" wich take one argement
    #step 1:take the len of text give it
    #step 2:len of text divide by 2
    #step 3:do two variable is name part 1 wich take the first part and part 2 wich take second variable
    #step 4:return the variable part1 , part2
#Part 3:creat a function his name "remove_special_characters(orig_string: str)" wich take one argement
    #step 1:create a variable name "s_cha" wich use the string module (string.ascii_letters , string.digits + " ")
    #step 2: create a variable name "sentence" wich take the correct cha 
    #step 3:do a loop (for) wich cercle cha cha 
    #step 4:check if cha in s_cha : if true append in variable sentence
    #step 5 : return the sentence
#step 1:import the libery string wich take functions (string.ascii_letters , string.digits )

from string import ascii_letters, digits
#PART 1:creat a function his name "change_case(orig_string: str)" wich take one argement 
def change_case(orig_string: str)->str:
    sentence = []
    #step 1:use a for loop to change a cha
    for cha in orig_string:
        #step 2:check if cha is lower_case change in uppercase or reverse and append in the list "sentence"
        if cha == cha.lower():
            sentence.append(cha.upper())
        else: 
            sentence.append(cha.lower())
    #step 3:return the sentence 
    return "".join(sentence)

#Part 2:creat a function his name "split_in_half(orig_string: str)" wich take one argement
def split_in_half(orig_string: str)-> str:
    #step 1:take the len of text give it
    medium_index = len(orig_string) // 2 #step 2:len of text divide by 2
    #step 3:do two variable is name part 1 wich take the first part and part 2 wich take second variable
    part1, part2 = orig_string[:medium_index] , orig_string[medium_index:]
    #step 4:return the variable part1 , part2
    return part1, part2

#Part 3:creat a function his name "remove_special_characters(orig_string: str)" wich take one argement
def remove_special_characters(orig_string: str)->str:
    #step 1:create a variable name "s_cha" wich use the string module (string.ascii_letters , string.digits + " ")
    s_cha = f"{ascii_letters} {digits}"
    #step 2: create a variable name "sentence" wich take the correct cha 
    sentence = []
    #step 3:do a loop (for) wich cercle cha cha 
    for cha in orig_string:
        #step 4:check if cha in s_cha : if true append in variable sentence
        if cha in s_cha:
            sentence.append(cha)
    #step 5 : return the sentence
    return "".join(sentence)
        
if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)