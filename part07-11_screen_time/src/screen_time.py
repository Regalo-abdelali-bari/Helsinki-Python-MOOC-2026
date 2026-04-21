# Write your solution here
# Write your solution here
from datetime import datetime , timedelta
def time_pass ():
    data_days = {}
    data_time = {}
    sum_time = []
    try:
        name_file = input("Filename: ")
        start = input("Starting date: ")
        days_spend = int(input("How many days: "))
        date = datetime.strptime(start,"%d.%m.%Y")
        print("Please type in screen time in minutes on each day (TV computer mobile):")

    except ValueError:
        print("you do a wrong tap.")
    num_day = 0
    for i in range(days_spend):
        day = timedelta(days = num_day)
        date += day
        string_day = f"day{i + 1}"
        time_spend = input(f"Screen time {date.strftime("%d.%m.%Y")}: ")
        minute = time_spend.split()
        data_days[string_day] = date
        data_time[string_day] = "/".join(minute)
        result = 0
        num_day = 1
        for num in minute:
            result += int(num)
        sum_time.append(result)

    with open(name_file,"w") as my_file:
        my_file.write(f"Time period: {data_days["day1"].strftime("%d.%m.%Y")}-{data_days[f"day{days_spend}"].strftime("%d.%m.%Y")}\n")
        my_file.write(f"Total minutes: {sum(sum_time)}\n")
        my_file.write(f"Average minutes: {sum(sum_time)/len(sum_time)}\n")
        for date , time in data_days.items():
            my_file.write(f"{time.strftime("%d.%m.%Y")}: {data_time[date]}\n")
    print(f"Data stored in file {name_file}")
    
time_pass()

