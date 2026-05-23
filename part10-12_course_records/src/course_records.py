# tee ratkaisusi tänne
class Course:
    def __init__(self):
        self.__courses = {}

    def add_course(self,name:str,grade:int,credit:int) : 
        if not name in self.__courses:
            self.__courses[name] = [grade,credit]
        elif grade > self.__courses[name][0]:
            self.__courses[name] = [grade,credit]
        

    def get_course(self,name):
        if not name in self.__courses:
            return None
        return self.__courses[name]

    def sum_credits(self):
        value = 0
        for credit in self.__courses.values():
            value += credit[1]
        return value

    def grades(self):
        self.__grades = {}
        
        for i in range(1,6):
            self.__grades[i] = ""
        for grade in self.__courses.values():
            self.__grades[grade[0]] += "x"

        return self.__grades

    def sum_grades(self):
        value = 0
        for grade in self.__courses.values():
            value += grade[0]
        return value
    def number_courses(self):
        return len(self.__courses)

class UserInterface:
    def __init__(self):
        self.__courses = Course()
    
    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__courses.add_course(name,grade,credit)

    def get_data_course(self):
        name = input("course: ")
        data = self.__courses.get_course(name)
        if data == None:
            print("no entry for this course")
        else:
            print(f"{name} ({data[1]} cr) grade {data[0]}")

    def statistics(self):
        print(f"{self.__courses.number_courses()} completed courses, a total of {self.__courses.sum_credits()} credits")
        print(f"mean {self.__courses.sum_grades() / self.__courses.number_courses():.1f}")
        print("grade distribution")
        grades = self.__courses.grades()
        i = 5
        while i > 0:
            print(f"{i}: {grades[i]}")
            i -= 1
            


    def search(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_data_course()
            elif command == "3":
                self.statistics()
            else:
                self.help()
            
course = UserInterface()
course.search()