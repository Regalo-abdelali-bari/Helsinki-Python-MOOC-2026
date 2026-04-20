# Write your solution here
import datetime
day = int(input("Day: "))
month = int(input("Month "))
year = int(input("Year: "))
user_birth = datetime.datetime(year,month,day)
the_even_year = datetime.datetime(1999,12,31)
if user_birth < the_even_year:
    print(f"You were {(the_even_year - user_birth).days} days old on the eve of the new millennium.")
else:
    print(f"You weren't born yet on the eve of the new millennium.")
