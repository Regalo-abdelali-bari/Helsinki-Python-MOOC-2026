# Write your solution here
def longest_series_of_neighbours(my_list: list):
    last_item = my_list[0]
    longer_serie = 1
    count = 1
    for item in my_list :
        if item == last_item -1 or item == last_item +1:
            count += 1
        else:
            count = 1
        if count > longer_serie :
            longer_serie = count
        last_item = item
    return longer_serie
if __name__ == "__main__":
    print(longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))
