# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
student_namesi = {}
exercices_numbers = {}
with open(student_info) as students:
    for student in students:
        student = student.strip().split(";")
        if student[0]  == "id":
            continue
        student_namesi[student[0]] = student[1] + " "+student[2]

with open(exercise_data) as exercices:
    for exercice in exercices:
        exercice = exercice.strip().split(";")

        if exercice[0] == "id":
            continue
        points = 0
        for point in exercice[1:]:
            points += int(point)
        exercices_numbers[exercice[0]]= points

for idei , name in student_namesi.items():
    if idei in exercices_numbers:
        point = exercices_numbers[idei]
        print(f"{name} {point}")
        