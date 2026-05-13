# Write your solution here:
class Item:
    def __init__ (self , name:str , weight:int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__ (self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self,max_weight : int):
        self.max_weight = max_weight
        self.__books = {}
        self.__books["w"] = 0
        self.__books["books"] = []
    def add_item(self , item : Item):
        m_w = self.max_weight
        if self.__books["w"] + item.weight() < m_w :
            self.__books["books"].append(item)
            self.__books["w"] += item.weight()

    def print_items(self):
        for item in self.__books["books"]:
            print(item)

    def weight(self):
        return self.__books["w"]

    def heaviest_item(self):
        if len(self.__books["books"]) == 0:
            return None
        heaviast = self.__books["books"][0]
        for book in self.__books["books"]:
            if heaviast.weight() < book.weight():
                heaviast = book
        return heaviast
    def __str__(self):
        return f"{len(self.__books["books"])} item ({self.__books["w"]} kg)" if len(self.__books["books"]) == 1 else f"{len(self.__books["books"])} items ({self.__books["w"]} kg)"
 
class CargoHold:
    def __init__(self,max_weight : int):
        self.__max = max_weight
        self.__books = []

    def add_suitcase(self,suite : Suitcase):
        if self.__max > suite.weight():
            self.__max -= suite.weight()
            self.__books.append(suite)

    def print_items(self):
        for books in self.__books:
            books.print_items()
    def __str__ (self):
        return f"{len(self.__books)} suitcase, space for {self.__max} kg" if len(self.__books) == 1 else f"{len(self.__books)} suitcases, space for {self.__max} kg"
if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

        