# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as people_data:
        data = people_data.read()
    
    data = json.loads(data)
    for items in data:
        for item in items:
            if item == "age":
                print(f"{items[item]} years ",end="")
            elif item == "hobbies":
                print("(",end="")
                for i in range(len(items[item])):
                    if i == len(items[item]) - 1:
                         print(f"{items[item][i]}",end="")
                    else:
                        print(f"{items[item][i]}, ",end="")
                print(")")
            else:
                print(items[item],end=" ")

if __name__ == "__main__":
    print_persons("file1.json")