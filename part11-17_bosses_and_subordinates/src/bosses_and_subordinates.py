# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    counter = 0
    if employee.subordinates == []:
        return 0

    for i in employee.subordinates:
        counter  += count_subordinates(i)

    counter += len(employee.subordinates)

    return counter