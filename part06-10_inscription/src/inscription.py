# Write your solution here

name = input("Whom should I sign this to: ")
my_file = input("Where shall I save it: ")
with open(my_file,"w") as file:
    file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")