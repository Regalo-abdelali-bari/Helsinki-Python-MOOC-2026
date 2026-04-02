# Write your solution here
def most_common_character(string: str):
    letter = string[0]
    count = string.count(letter)
    for cha in string:
        count1 = string.count(cha)
        if count >= count1:
            continue
        else:
            count = count1
            letter = cha
    return letter
if __name__ == "__main__":
    print(most_common_character("exemplaryelementary"))

