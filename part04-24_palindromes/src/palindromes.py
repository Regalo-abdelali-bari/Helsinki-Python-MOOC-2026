# Write your solution here

def palindromes(word1) :
    
    word = word1
    i = -1
    word2 = ""
    while True:
        while True:
            if len(word1) == len(word2):
                break
            word2 += word[i]
            
            word = word[:i]
        return word1 == word2

while True:
    mot = input("Please type in a palindrome: ")
    if palindromes(mot):
        print(mot,"is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")


    

 


        
        
        

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
