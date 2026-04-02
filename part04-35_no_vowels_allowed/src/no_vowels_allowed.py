# Write your solution here
# Write your solution here
def no_vowels(string: str):
    vowels = "aiuoe"
    for cha in string:
        if cha in vowels:
            string = string.replace(cha,"")
    return string
if __name__ == "__main__":
    print(no_vowels("this is an example"))