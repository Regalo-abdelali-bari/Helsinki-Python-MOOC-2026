
def first_word(sentence):
    index = 1
    while sentence[index] != " ":
        word1= sentence[:index+1]
        index += 1
    return word1
def second_word(sentence):
    find = sentence.find(" ")
    index = find + 2
    while sentence[index] != " " and len(sentence)-1>index:
        if sentence[index+1] == " ":
            word2= sentence[find +1:index+1]
        elif  sentence[index+1] != " ":
            word2= sentence[find +1:index+2]
        index += 1
    return word2
def last_word(sentence):
    
    
    while True:
        find = sentence.find(" ")
        if find == -1:
            break
        sentence= sentence[find +1:]
        find += 1
        

    return sentence

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    