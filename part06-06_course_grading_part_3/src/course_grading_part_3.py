# tee ratkaisu tänne
# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_point=input("Exam points: ")
student_names = {}
exercices_numbers = {}
exam_points ={}
with open(student_info) as students:
    for student in students:
        student = student.strip().split(";")
        if student[0]  == "id":
            continue
        student_names[student[0]] = student[1] + " "+student[2]

with open(exercise_data) as exercices:
    for exercice in exercices:
        exercice = exercice.strip().split(";")

        if exercice[0] == "id":
            continue
        points = 0
        for point in exercice[1:]:
            
            points += int(point)

        points1 =  ((points/40 )*100 )//10
        exercices_numbers[exercice[0]]= [points , int(points1)]


with open(exam_point) as exams:
    for exam in exams:
        exam = exam.strip().split(";")
        if exam[0] == "id":
            continue
        points = 0
        for point in exam[1:]:
            points += int(point)
        exam_points[exam[0]]= points 
i = 0
for key , value in student_names.items():
    if i == 0:
        print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}grade")
        i += 1
    name = student_names[key]
    num = exercices_numbers[key][0]
    point = exercices_numbers[key][1]
    point1 = exam_points[key]
    points = point1 + point
    if points < 15:
        grade = 0
    elif points < 18 :
        grade = 1
    elif points < 21 :
        grade = 2
    elif points < 24 :
        grade = 3
    elif points < 28 :
        grade = 4
    else : 
        grade = 5
    print(f"{name:30}{num:<10}{point:<10}{point1:<10}{points:<10}{grade}")
#students1.csv
#exercises1.csv
#exam_points1.csv