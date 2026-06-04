class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here
def names_of_students(attempts: list):
    return map(lambda item: item.student_name , attempts)

def course_names(attempts: list):
    my_list1 = []
    my_list = sorted(list(map(lambda item: item.course_name , attempts)))
    for item in my_list :
        if item not in my_list1:
            my_list1.append(item) 
    return my_list1


