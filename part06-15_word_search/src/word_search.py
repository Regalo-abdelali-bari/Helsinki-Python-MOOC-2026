# Write your solution here
def find_words(search_term: str):
    my_list = []
    with open("words.txt") as my_file:
        for word in my_file:
            word= word.strip()
            if "*" in search_term :
                if search_term.startswith("*")  :
                    if word.endswith(search_term[1:]):
                        my_list.append(word)
                        continue
                else:
                    if word.startswith(search_term[:-1]):
                        my_list.append(word)
            elif "." in search_term :
                i = -1
                if len(word) == len(search_term):
                    for cha in search_term:
                        i += 1
                        if cha == "." or cha == word[i]:
                            words = True
                            continue
                        words = False
                        break
                    if words:
                        my_list.append(word)
            else:
                if word == search_term:
                    my_list.append(word)
                    break
    return my_list 


if __name__ == "__main__":
    print(find_words("ca*"))