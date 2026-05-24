# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self,number : int , lottery : list):
        self.w_n = number
        self.liste = lottery

    def number_of_hits(self,numbers: list):
        return len([number for number in numbers if number in self.liste])

    def hits_in_place(self,numbers):
        return [number if number in self.liste else -1 for number in numbers]
