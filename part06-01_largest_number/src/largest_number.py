# write your solution here
def largest():
    with open("numbers.txt") as numbers:
        item = 0
        for line in numbers:
            line = int(line)
            if line > item:
                item = line
        return item
if __name__ == "__main__":
    print(largest())