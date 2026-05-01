# Write your solution here
#step1 : import string (acsii_uppercase)
#step2 : do a function name "run(progrm:list)" wich take one argement (list)
#step3 : do a list wich take the data gives by user and sind it to the output its name output
#step4 : do three dictionarys wich the first has (ADD , SUB, MUL)  third a dictionary wich the key is the letters
#step5 : do a for loop wich do cha in acsii_uppercase and ubdate in third a dictionary
#step6 :do a while loop wich end when the exersion is "END"
#step7 : do a for loop wich cha in the list
#step8 : check if "MOV" in cha we split and take the it in the dctionary
#step9 : check elif "PRINT" in cha we split and append the second character in output
#step10 :check elif cha in (ADD , SUB, MUL) and do if all of them and calculate and change the value of variable
#step11 :check elif "IF" in cha we do the check and if yes we break the loop and change the program 
#step12 :elif "END" == cha break
#step13 : contunue

#step1 : import string (acsii_uppercase) and  import operator
from string import ascii_uppercase
import operator
#step2 : do a function name "run(progrm:list)" wich take one argement (list)
def run(syntax: list):
    #step3 : do a list wich take the data gives by user and sind it to the output its name output
    output = []
    #step4 : do two dictionarys wich
    operators = {       #the first has (ADD , SUB, MUL)
    "ADD": operator.add,
    "SUB": operator.sub,
    "MUL": operator.mul
    }
    letters = {} #second a dictionary wich the key is the letters
    #step5 : do a for loop wich do cha in acsii_uppercase and ubdate in third a dictionary
    for cha in ascii_uppercase:
        letters[cha] = 0
    
    #step6 :do a while loop wich end when the exersion is "END"
    if len(syntax) > 0:
        item =syntax[0]
    i = -1
    while len(syntax) > 0:
        #step7 : do a for loop wich cha in the list
        word = False
        while True:
            
            if "END" in item or i == len(syntax) - 1  :
                word = True
                break
            i += 1
            item = syntax[i]
            item = item.split()

            #step8 : check if "PRINT" in cha we split and append the second character in output
            if "PRINT" in item :
                if item[1] in letters:
                    num = letters[item[1]]
                else:
                    num = int(item[1])
                
                output.append(num)
            #step9 : check elif "MOV" in cha we split and take the it in the dctionary
            elif "MOV" in item:
                if item[2] in letters:
                    num = letters[item[2]]
                else:
                    num = int(item[2])
                letters[item[1]] = num
            #step10 :check elif cha in (ADD , SUB, MUL) and do if all of them and calculate and change the value of variable
            elif item[0] in ("ADD" , "SUB", "MUL"):
                if item[2] in letters:
                    num = letters[item[2]]
                else:
                    num = int(item[2])
                letters[item[1]] = operators[item[0]](letters[item[1]],num)
            #step11 :check elif "IF" in cha we do the check and if yes we break the loop and change the program 
            elif "JUMP" == item[0]:
                
                i = syntax.index(item[-1]+":")
                
                break
            elif "IF" == item[0]:
                if item[3] in letters:
                    num = letters[item[3]]
                else:
                    num = int(item[3])
                if item[2] == "<=":
                    if letters[item[1]] <= num:
                        i = syntax.index(item[-1]+":")
                        break
                elif item[2] == ">=":
                    if letters[item[1]] >= num:
                        i = syntax.index(item[-1]+":")
                        break
                elif item[2] == ">":
                    if letters[item[1]] > num:
                        i = syntax.index(item[-1]+":")
                        break
                elif item[2] == "<":
                    if letters[item[1]] < num:
                        i = syntax.index(item[-1]+":")
                        break
                elif item[2] == "==":
                    if letters[item[1]] == num:
                        i = syntax.index(item[-1]+":")
                        break
                elif item[2] == "!=":
                    if letters[item[1]] != num:
                        i = syntax.index(item[-1]+":")
                        break
                else:
                    continue
            #step13 : contunue
            else:
                continue
        
        if word:
            break
    return output

if __name__ == "__main__":
    program4 = []
    
    result = run(program4)
    print(result)