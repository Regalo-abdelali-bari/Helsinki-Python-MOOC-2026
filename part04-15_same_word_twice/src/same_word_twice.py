# Write your solution here
my_list = []
index = 0
while True:
    word = input("Word: ")
    if word in my_list:
        break
    index += 1
    my_list.append(word)
print(f"You typed in {index} different words")