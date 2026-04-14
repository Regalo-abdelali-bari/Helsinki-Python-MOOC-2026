# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        w_f=input("The word in Finnish: ")
        w_e=input("The word in English: ")
        with open("dictionary.txt","a") as my_file:
            my_file.write(f"{w_f} - {w_e}\n")
            print("Dictionary entry added")
    elif function == "2":
        search = input("Search term: ")
        with open("dictionary.txt") as my_file:
            for item in my_file:
                if search in item :
                    print(f"{item[:-1]}")
    else:
        print("Bye!")
        break

