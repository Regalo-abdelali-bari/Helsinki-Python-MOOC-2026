# Write your solution here
dict_users={}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3 :
        print("quitting...")
        break
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        print("ok!")
        dict_users[name]=number
    else:
        name = input("name: ")
        if name in dict_users:
            print(dict_users[name])
        else:
            print("no number")


