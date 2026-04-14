# Write your solution here
def read_input(sentence:str, num1 : int , num2 : int):
    while True:
        try:
            number = int(input(sentence))
        except ValueError:
            number = -1
        if num1 <= number  <= num2:return number
        else:print(f"You must type in an integer between {num1} and {num2}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)