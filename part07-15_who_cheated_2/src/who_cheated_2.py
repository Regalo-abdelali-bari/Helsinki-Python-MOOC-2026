# Write your solution here
import csv
from datetime import datetime,timedelta

def calculate_time(time:list): #calculate_time this function help you to calculate time between start and finish
    time_start = datetime.strptime(time[0],"%H:%M")
    time_finish = datetime.strptime(time[1],"%H:%M")


    return time_finish - time_start


def final_points():
    students_data = {}
    clean_data = {}
    with open("start_times.csv") as time_start:
        for line in csv.reader(time_start,delimiter=";"):
            students_data[line[0]] = {"time_start":line[1]}
    with open("submissions.csv") as time_finish:
        for line in csv.reader(time_finish,delimiter=";"):
            if line[1] in students_data[line[0]]:
                if students_data[line[0]][line[1]][0] < int(line[2]) and calculate_time([students_data[line[0]]["time_start"] ,line[-1]]) <= timedelta(hours=3):
                    students_data[line[0]][line[1]]=[int(line[2]),line[3]]
            else:
                students_data[line[0]].update({line[1]:[int(line[2]),line[3]]})

    for name,data in students_data.items():
        points_total = 0
        
        for items in data.values():
            if len(items) > 2:
                continue
            
            
            points_total += items[0]
        
        clean_data[name] = points_total
    return clean_data

if __name__ == "__main__":
    print(final_points())