# Copy here code of line function from previous exercise and use it in your solution
def line(num, string):
    if string == "":
        print("*"*num)
    else:
        print(string[0] * num)
def shape(num1, string1, num2, string2):
    times = 1
    times1 = 1
    while times <= num1 and not string1 == "":
        line(times,string1)
        times += 1
    while times1 <= num2 and not string2 == "":
        line(num1,string2)
        times1 += 1
       
        
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "")