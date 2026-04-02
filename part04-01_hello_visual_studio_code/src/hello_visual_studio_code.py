# Write your solution here
while True:
    word=input("Editor: ")
    if "visual studio code" == word.lower():
        break
    elif word.lower() in ("notepad","word") : 
        print("awful")
    else:
        print("not good")
print("an excellent choice!")
