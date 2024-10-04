# Guessing Game by Motiur Rahman Mizan
# Code written at 17:15:35; Oct 04, 2024

from random import randint, choice

class Game:
    win = ["Congratulations", "Welcome", "Fantastic", "Amazing", "Nice"]
    lose = ["Opps", "Sorry", "Alas"]
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def take_input(self):
        inp = input(f"Type your guess between {self.start} and {self.end}: ")
        if inp.isnumeric():
            if int(inp)>=self.start and int(inp)<=self.end:
                return int(inp)
        print(f"Oh, no. Type an integer between {self.start} and {self.end}")
        return self.take_input()
    
    def check_guess(self, gen_int, user_int):
        return gen_int == user_int
    
    
    def start_game(self):
        for _ in range(5):
            random = randint(self.start, self.end)
            inp = self.take_input()
            if self.check_guess(random, inp):
                print(f"{choice(self.win)}! You win the game!")
            else:
                print(f"{choice(self.lose)}! You lose the game")
            
            print()



game = Game(1, 6)
game.start_game()