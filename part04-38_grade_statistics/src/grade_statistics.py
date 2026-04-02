# Write your solution here
def inputs_of_user():
    points = []
    exercices1 = []
    while True:
        points_and_exercices = input("Exam points and exercises completed: ")
        if points_and_exercices == "":
            break
        if int(points_and_exercices[:2]) >= 21 or int(points_and_exercices[2:]) >= 101:
            break
        points.append(float(points_and_exercices[:2]))
        exercices1.append(float(points_and_exercices[2:]))
    return [points,exercices1]
def calculate_points(points1: list):
    i = 0
    exercices1 = points1[-1]
    points= points1[0]
    point2 = points.copy()
    for exercice in exercices1:
        add_points = exercice // 10
        points[i] += add_points
        i += 1
    return [points , point2]
def result_perstange(points1 : list):
    person_pass = 0 
    points = points1[-1]
    points3 = points1[0]
    i = 0
    for point in points:
        if point  > 9 and points3[i] > 14:
            person_pass += 1
        i += 1
    percentage_class =(person_pass / len(points))*100 
    return f"Pass percentage: {percentage_class:.1f}" 
def max_points(points: list):
    i = sum(points[0]) / len(points[0])
    return f"Statistics:\nPoints average: {i}"
def grade(points1: list):
    points = points1[0]
    point1 = points1[-1]
    grade0="  0: "
    grade1="  1: "
    grade2="  2: "
    grade3="  3: "
    grade4="  4: "
    grade5="  5: "
    i = 0
    for point in points:
        if point1[i] < 10 or point <= 14:
            grade0+="*"
        elif 27< point <= 30:
            grade5 +="*"
        elif 23< point <= 27:
            grade4 +="*"
        elif 20< point <= 23:
            grade3 +="*"
        elif 18<= point <= 20:
            grade2 +="*"
        elif 15<= point <= 17 :
            grade1 +="*"
        i += 1
    return f"Grade distribution:\n{grade5}\n{grade4}\n{grade3}\n{grade2}\n{grade1}\n{grade0}"
def main():
    inputs = inputs_of_user()
    point = calculate_points(inputs)
    point1 = max_points(point)
    print(point1)
    mean=result_perstange(point)
    print(mean)
    grade_class = grade(point)
    print(grade_class)
main()
    



                    
        




    
    