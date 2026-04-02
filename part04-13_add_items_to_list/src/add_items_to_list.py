# Write your solution here
items = int(input("How many items: "))
my_list=[]
index = 1 
while index <= items :
    item = int(input(f"Item {index}: "))
    my_list.append(item)
    index += 1
print(my_list)