# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_list = []
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
   # add a second argument to the function call
    handle_file = urllib.request.urlopen(address)
   # the rest of your function
    
    data_courses = handle_file.read()
    data_courses = json.loads(data_courses)
    for data in data_courses:
        if data[ "enabled"]:
            course = data["fullName"]
            name = data["name"]
            year = data["year"]
            sum_exercices = sum(data["exercises"])
            my_list.append((course,name,year,sum_exercices))
    return my_list


def retrieve_course(course_name: str):
    students = 0
    hours = 0
    exercices = 0
    # the rest of your function
    handle_file =urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data_course = handle_file.read()
    data_course = json.loads(data_course)
    for small_data in data_course:
        if students < data_course[small_data]["students"]:
            students = data_course[small_data]["students"]
        hours += data_course[small_data]["hour_total"]
        exercices += data_course[small_data]["exercise_total"]
    week = len(data_course)
    exercise_averge = int(exercices / students)
    hours_averge = int(hours / students)
    return {'weeks': week,
        'students': students,
        'hours': hours,
        'hours_average': hours_averge,
        'exercises': exercices,
        'exercises_average': exercise_averge
    }

        
        
if __name__ == "__main__":
    print(retrieve_course("docker2019"))