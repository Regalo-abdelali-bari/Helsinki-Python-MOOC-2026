# Write your solution here
dict_users={}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3 :
        print("quitting...")
        break
    name = input("name: ")
    
    if command == 2:
        
        number = input("number: ")
        print("ok!")
        dict_users.setdefault(name,[]).append(number)

    else:
        if name in dict_users:
            print("\n".join(dict_users[name]))
        else:
            print("no number")