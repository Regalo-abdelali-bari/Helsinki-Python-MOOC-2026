# write your solution here
text = input("Write text: ")
with open("wordlist.txt") as wo_c:
    wo_c=wo_c.read().replace("\n"," ").split()
    text = text.split()
    for word in text:
        if word.lower() in wo_c:
            print(word,end=" ")
            continue
        else:
            print(f"*{word}*",end=" ")
