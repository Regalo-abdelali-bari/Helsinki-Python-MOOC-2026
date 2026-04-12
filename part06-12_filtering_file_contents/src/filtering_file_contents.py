# Write your solution here
def filter_solutions():
    my_list = []
    result = 0
    with open("correct.csv","w") as c:
        pass
    with open("incorrect.csv","w") as ic:
        pass
    with open("solutions.csv") as opertions:
        for opertion in opertions:
            opertion = opertion.split(";")
            my_list.append(opertion)
    for items in my_list:
        if "+" in items[1]:
            i = items[1].split("+")
            for item in i :
                result += int(item)
        else:
            i = items[1].split("-")
            for item in i:
                if result == 0:
                    result += int(item)
                else:
                    result -= int(item)
        line = ""
        for item in items:
            line += f"{item};"
        line = line[:-1]
        if result == int(items[2]):
            with open("correct.csv","a") as correct:
                correct.write(line)
        else:
            with open("incorrect.csv","a") as incorrect:
                incorrect.write(line)
        result = 0
if __name__ == "__main__":
    filter_solutions()