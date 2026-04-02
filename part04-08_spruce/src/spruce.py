# Write your solution here
def spruce(num):
    times = 1
    string = "*"
    print('a spruce!')
    while times <= num:
        print(" "*(num - times)+string)
        string += "**"
        times += 1 
    print(" "*(num-1)+"*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

    