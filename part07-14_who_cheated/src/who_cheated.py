# Write your solution here
import csv
from datetime import datetime,timedelta
def calculate_time(time:list):
    time_start = datetime.strptime(time[0],"%H:%M")
    time_finish = datetime.strptime(time[1],"%H:%M")
    for time_f in time[2:]:
        if datetime.strptime(time_f,"%H:%M") > time_finish:
            time_finish = datetime.strptime(time_f,"%H:%M")
    return time_finish - time_start

def cheaters():
    students_time = {}
    list_cheaters =[]
    #we open the file and we take the name and time start a task
    with open("start_times.csv") as time_start:
        for line in csv.reader(time_start,delimiter=";"):
            students_time[line[0]] = [line[1]]
    #we open the file and we add time finish a task in students_time
    with open("submissions.csv")  as time_finish:
        for line in csv.reader(time_finish,delimiter=";"):
            students_time[line[0]].append(line[-1])

    for name,time in students_time.items():
        hours_taking = calculate_time(time)
        
        if hours_taking > timedelta(hours=3):
            list_cheaters.append(name)
    return list_cheaters

if __name__ == "__main__":
    print(cheaters())
        
