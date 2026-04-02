# Write your solution here
def histogram(string: str):
    d = {}
    for cha in string:
        if cha not in d:
            d[cha]=""
        d[cha]+="*"
    
    for key,value in d.items():
        print(key,value)

    