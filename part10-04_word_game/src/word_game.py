# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word): return 1  
        elif len(player1_word) < len(player2_word): return 2  
        else : pass

class MostVowels(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)

    def __count_vowel(self,word):
        num_vowel = 0
        for i in word:
            if i in "aieuo":
                num_vowel += 1  
        return num_vowel

    def round_winner(self, player1_word: str, player2_word: str):
        p1 = 0
        p2 = 0
        for i in player1_word:
            if i in "aieuo":
                p1 += 1
        for i in player2_word:
            if i in "aieuo":
                p2 += 1
        if p1 > p2:return 1
        elif p1 < p2:return 2
        else:pass

class RockPaperScissors(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        methods = ("rock","paper","scissors")
        
        if player1_word == "rock" and player2_word == "scissors":
            return 1
        
        elif player1_word == "paper" and player2_word == "rock":
            return 1

        elif player1_word == "scissors" and player2_word == "paper":
            return 1

        elif player2_word == "rock" and player1_word == "scissors":
            return 2
        
        elif player2_word == "paper" and player1_word == "rock":
            return 2

        elif player2_word == "scissors" and player1_word == "paper":
            return 2
        
        if player1_word not in methods and player2_word not in methods:
            return 0
        if player1_word not in methods:
            return 2
        if player2_word not in methods:
            return 1
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()    
    #rock
#boat
#dynamite
#scissors
#car
#bike