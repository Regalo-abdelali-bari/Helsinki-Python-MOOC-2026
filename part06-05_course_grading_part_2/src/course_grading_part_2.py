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
        points = ((points/40 )*100 )//10
        exercices_numbers[exercice[0]]= points


with open(exam_point) as exams:
    for exam in exams:
        exam = exam.strip().split(";")
        if exam[0] == "id":
            continue
        points = 0
        for point in exam[1:]:
            points += int(point)
        exam_points[exam[0]]= points

for key , value in student_names.items():
    if key in exercices_numbers:
        point = exercices_numbers[key]
    if key in exam_points:
        point += exam_points[key]
    if point < 15:
        print(f"{student_names[key]} 0")
    elif point < 18 :
        print(f"{student_names[key]} 1")
    elif point < 21 :
        print(f"{student_names[key]} 2")
    elif point < 24 :
        print(f"{student_names[key]} 3")
    elif point < 28 :
        print(f"{student_names[key]} 4")
    else : 
        print(f"{student_names[key]} 5")
#students1.csv
#exercises1.csv
#exam_points1.csv