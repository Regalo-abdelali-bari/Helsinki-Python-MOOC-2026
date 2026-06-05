# Write your solution here
import re

def is_dotw(my_string: str):
 
    return True if my_string in ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun") else False



def all_vowels(my_string: str):

    return True if re.search("^[aeiuo]+$",my_string) else False

def time_of_day(my_string: str):
    time1 =  re.search("[0-1][0-9]:[0-5][0-9]:[0-5][0-9]",my_string)
    time2 =  re.search("[0-2][0-4]:[0-5][0-9]:[0-5][0-9]",my_string)
    return True if time1 or time2 else False
