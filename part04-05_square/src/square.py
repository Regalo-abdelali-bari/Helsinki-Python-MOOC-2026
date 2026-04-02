# Copy here code of line function from previous exercise
def line(num, string):
    if string == "":
        print("*"*num)
    else:
        print(string[0] * num)
def square(size, character):
    # You should call function line here with proper parameters
    times = 0
    while True :
        if times == size:
            break
        line(size, character)
        times +=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")