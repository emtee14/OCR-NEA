import json
import os
import time
from pyfiglet import figlet_format

class music_game():
    def __init__(self):
        with open("./Music-Game/info.json", "r") as f:
            self.game_info = json.load(f)
            self.tracks = self.game_info["songs"]
            self.leaderboard = sorted(self.game_info["leaderboard"], key = lambda x: x[1], reverse=True)
        self.score = 0
        self.max_guess = 2

    def _clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _home(self, score=None):
        self._clear_terminal()
        print(figlet_format('Music Game'))
        if score:
            print(f"Your Score - {self.score}")
        print("Options:")
        print("1 - View Leaderboard")
        print("2 - Play The Game")
        print("3 - Exit")
        option = input("> ").replace(" ", "")
        if option == "1":
            self._leaderboard()
        elif option == "2":
            self._main_game()
        else:
            exit()

    def _leaderboard(self):
        self._clear_terminal()
        print(figlet_format('Leaderboard'))
        for i in self.leaderboard[:5]:
            print(f"{self.leaderboard.index(i)+1}. {i[1]} Points By {i[0].title()} ")
        print("Enter q To Go Back")
        if input("> ").lower().replace(" ", "") == "q":
            self._home()
        else: exit()

    def _main_game(self):
        self._clear_terminal()
        self.score = 0
        print(figlet_format('Music Game'))
        self.name = input("Your Name - ").title()
        for i in self.tracks:
            letters = ""
            for x in i[0].split(" "):
                under = "_"*int(len(x)-1)
                letters = letters + x[0].upper() + under + " "
            print(f"Question {self.tracks.index(i) + 1} - {i[1]} {letters}")
            answer = input("> ")
            if answer.lower() == i[0].lower():
                self.score += 3
            else:
                print("1 Guess Left")
                answer = input("> ")
                if answer.lower() == i[0].lower():
                    self.score += 2
                else:
                    break
        self._clear_terminal()
        print(figlet_format('Game Over'))
        time.sleep(1.5)
        self._end()

    def _end(self):
        with open("Music-Game/info.json", "w") as f:
            self.game_info["leaderboard"].append([self.name, self.score])
            json.dump(self.game_info, f, indent=4)
        self.leaderboard = sorted(self.game_info["leaderboard"], key = lambda x: x[1], reverse=True)
        self._clear_terminal()
        self._home(score=self.score)     

    def run(self):
        self._home()
