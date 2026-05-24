# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        f = f.read().strip()
        sentence = "".join(cha for cha in f if cha not in ".,?!:;").split()
        
    
    
    return {word:sentence.count(word) for word in sentence if sentence.count(word) >= lower_limit }
    

if __name__ == "__main__":
    most_common_words("comprehensions.txt", 3)