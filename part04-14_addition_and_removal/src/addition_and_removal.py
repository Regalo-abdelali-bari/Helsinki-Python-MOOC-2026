# Write your solution here
my_list=[]
index = 0
while True:
    print(f"The list is now {my_list}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "x" :
        break
    elif operation == "d":
        index += 1
        my_list.append(index)
    elif operation == "r" and index >0:
        my_list.pop(-1)
        index -=1
    
print("Bye!")
