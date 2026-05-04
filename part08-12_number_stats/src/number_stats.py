# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
    def add_number(self, number:int):
        self.numbers += number
        self.count += 1
        return self.numbers
    def count_numbers(self):
        return self.count

    def get_sum(self):
        return self.numbers if self.numbers > 0 else 0

    def average(self):
        return self.numbers / self.count if self.numbers > 0 else 0

def main():
    print("Please type in integer numbers:")
    numbers = NumberStats()
    numbers_even = NumberStats()
    numbers_odd = NumberStats()
    while True:
        user_num = int(input(""))
        if user_num <= -1:
            break
        numbers.add_number(user_num)
        numbers_even.add_number(user_num) if user_num % 2 == 0 else numbers_odd.add_number(user_num)
    print("Sum of numbers:",numbers.get_sum())
    print("Mean of numbers:",numbers.average())
    print("Sum of even numbers:",numbers_even.get_sum())
    print("Sum of odd numbers:",numbers_odd.get_sum())

main()
