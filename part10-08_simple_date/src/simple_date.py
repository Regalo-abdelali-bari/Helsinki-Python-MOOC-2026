# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, days:int, months:int, years:int):
        self.days = days
        self.months = months
        self.years = years

    def __days(self):
        return (self.years * 360 ) + (self.months * 30) + self.days

    def __eq__(self,another):
        return self.__days() == another.__days()

    def __ne__(self,another):
        return self.__days() != another.__days()
    
    def __gt__(self,another):
        return self.__days() > another.__days()

    def __lt__(self, another):
        return self.__days() < another.__days()

    def __add__(self,another):
        result = SimpleDate(self.days,self.months,self.years)
        for i in range(another):
            if result.days == 30:
                result.days = 1
                if result.months == 12:
                    result.months = 1
                    result.years += 1
                else:
                    result.months += 1
            else:
                result.days += 1
        return result

    def __sub__(self,another):
        return self.__days() - another.__days() if self.__days() > another.__days() else another.__days() - self.__days()
    def __str__(self):
        return f"{self.days}.{self.months}.{self.years}"
    
if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)