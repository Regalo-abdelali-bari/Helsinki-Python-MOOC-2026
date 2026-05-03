# Write your solution here:
class Pet:
    def __init__ (self , n : str , s :str , y_b : int):
        self.name = n
        self.species = s
        self.year_of_birth = y_b
    
def new_pet(name: str, species: str, year_of_birth: int):
    animal = Pet(name , species , year_of_birth)
    return animal

if __name__ == "__main__":
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)