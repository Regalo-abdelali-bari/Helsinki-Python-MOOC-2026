# Write your solution here
def range_of_list(items:list):
    return max(items) - min(items)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 6, 9]
    result = range_of_list(my_list)
    print(result)