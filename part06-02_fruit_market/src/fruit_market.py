# write your solution here
def read_fruits():
    with open("fruits.csv") as fruits:
        d = {}
        for fruit in fruits:
            fruit = fruit.replace(";"," ")
            fruit = fruit.split()
            d[fruit[0]]=float(fruit[1])
            
    return d
            
if __name__ == "__main__":
    print(read_fruits())