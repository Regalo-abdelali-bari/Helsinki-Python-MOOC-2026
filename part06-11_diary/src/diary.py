# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")
    if function == "1":
        with open("diary.txt","a") as file:
            sentence = input("Diary entry: ")
            file.write(f"{sentence}\n")
            print("Diary saved")
    elif function == "2":
        with open("diary.txt") as file:
            print("Entries:")
            for line in file:
                line= line.strip()
                print(line)
    else:
        print("Bye now!")
        break
        
