# Write your solution here
def oldest_person(people: list):
    item = people[0]
    for old in people:
        if old[-1] < item[-1]:item = old
    return item[0]