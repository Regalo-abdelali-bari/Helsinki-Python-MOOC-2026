# Write your solution here
#step 1:open the file and do list of faulte word
#step 2:give the user a input to write his text
#step 3:cheak if all words in file
#step 4:append the false word in a list
#step 5:print what is the fault in the sentence
#step 6:use the function "get_close_matches"
#step 7:print: the words close
import difflib
def spell_checker():
    #step 1:open the file and do list of faulte word
    faulte_word = []
    with open("wordlist.txt") as f:
        wo_c=f.read().replace("\n"," ").split()
        #step 2:give the user a input to write his text
        text = input("write text: ").split()
        #step 3:cheak if all words in file
        for word in text:
            if word.lower() not in wo_c:
                #step 4:append the false word in a list
                faulte_word.append(word)
            #step 5:print what is the fault in the sentence
                print(f"*{word}*",end=" ")
            else:
                print(word,end=" ")
        print()
        #step 6:use the function "get_close_matches"
        print("suggestions:")
        for word in faulte_word:
            word_close = difflib.get_close_matches(word,wo_c)
            #step 7:print: the words close
            print(f"{word}: {", ".join(word_close)}")


spell_checker()