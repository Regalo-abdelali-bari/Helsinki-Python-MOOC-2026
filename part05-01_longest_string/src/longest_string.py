# Write your solution here
def longest(strings: list):
    longer_word = strings[0]
    for word in strings:
        if len(word) > len(longer_word):
            longer_word = word
    return longer_word