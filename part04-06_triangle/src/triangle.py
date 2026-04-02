# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        print("*"*num)
    else:
        print(string[0] * num)
def triangle(size):
    # You should call function line here with proper parameters
    #times = size - 1
    #while times >= 0:
        #line(size - times, "#")
        #times -= 1
    times = 1
    while times <= size:
        line(times, "#")
        times += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
