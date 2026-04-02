# Write your solution here
def formatted(my_list: list):
    list_my = []
    for item in my_list:
        list_my.append(f"{item:.2f}")
    return list_my

if __name__ == "__main__":
    
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))
