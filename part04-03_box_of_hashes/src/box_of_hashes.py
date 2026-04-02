# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        print("*"*num)
    else:
        print(string[0] * num)
def box_of_hashes(height):
    # You should call function line here with proper parameters
    times = 0
    while  times < height :
        line(10, "#")
        times += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
