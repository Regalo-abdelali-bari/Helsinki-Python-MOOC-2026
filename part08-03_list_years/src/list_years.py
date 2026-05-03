# Write your solution here
# Remember the import statement
# from datetime import date
from datetime import date
def list_years(dates: list):
    years_list = []
    for date in dates:
        years_list.append(date.year)
    return sorted(years_list)
