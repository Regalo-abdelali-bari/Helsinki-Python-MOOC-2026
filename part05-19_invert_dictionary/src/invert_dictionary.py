# Write your solution here
def invert(dictionary: dict):
    d = {}
    for key,value in dictionary.items():
        d[value]=key
    dictionary.clear()
    for key,value in d.items():
        dictionary[key]=value

    