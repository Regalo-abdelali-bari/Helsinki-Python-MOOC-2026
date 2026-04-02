# Write your solution here
def length_of_longest(items: list):
    longer = len(items[0])
    for item in items:
        if len(item) > longer:
            longer = len(item)
    return longer

