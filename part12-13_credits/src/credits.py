from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts:list):
    return reduce(lambda sum_numbers , number : sum_numbers + number.credits , attempts,0)

def sum_of_passed_credits(items):
    return reduce(lambda sum_numbers , number : sum_numbers + number.credits , list(filter(lambda item: item.grade > 0,items)), 0)

def average(items):
    my_list = list(filter(lambda item: item.grade > 0,items))
    return reduce(lambda sum_numbers , number : sum_numbers + number.grade ,my_list, 0) / len(my_list)

