# Write your solution here
def new_person(name: str, age: int):
    if 0 <= age <= 150:
        if 0 < len(name) <= 40  and len(name.split()) >= 2:
            return name , age
    
    raise ValueError
if __name__ == "__main__":
    print(new_person('Tim Andrew Smith', 97))
            
