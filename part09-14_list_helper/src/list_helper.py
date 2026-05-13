# WRITE YOUR SOLUTION HERE:

class ListHelper:
    

    @classmethod
    def greatest_frequency(cls,my_list: list):
        the_great = 0
        num = 0
        for number in my_list:
            if the_great < my_list.count(number):
                the_great = my_list.count(number)
                num = number
        return num



    @classmethod
    def doubles(cls,my_list: list):
        numbers_twice = 0
        numbers_count = []
        for number in my_list:
            if my_list.count(number) >= 2 and number not in numbers_count:
                numbers_twice += 1
                numbers_count.append(number)
        return numbers_twice

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))


