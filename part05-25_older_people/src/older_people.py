# Write your solution here
def older_people(people: list, year: int):
    items = []
    for old in people:
        if old[1] < year:items.append(old[0])
    return items