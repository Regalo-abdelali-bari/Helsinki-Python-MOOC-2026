# Write your solution here
class Checklist:
    def __init__ (self , header : str , entries : list):
        self.header = header
        self.entries = entries
    
class Customer:
    def __init__ (self , id : str, balance : float ,discount : int):
        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:
    def __init__ (self , m :str , l : float , m_s : int , b : bool):
        self.model = m
        self.length = l
        self.max_speed = m_s
        self.bidirectional = b