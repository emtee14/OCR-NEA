import os
import random
import time

from pyfiglet import figlet_format


class dice_game():

    def __init__(self):
        self.ROUNDS = 5
        self.logged_in = False
        self.p1_score = 0
        self.p2_score = 0
        self.dice_1 = None
        self.dice_2 = None
        self.users = []
        with open("./DIce-Game/users.txt") as f:
            for i in f:
                self.users.append(i.replace("\n", "").split(":"))

    def _clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _login(self, user=1):
        self._clear_terminal()
        print(f"{figlet_format('Dice Game')} \nPlayer {user} Login - ")
        username = input("\tUsername - ")
        password = input("\tPassword - ")
        user_pass = [username, password]
        if user_pass in self.users:
            print(f"Player {user} Succesfully Logged In")
            time.sleep(1.5)
            if user == 1:
                self._login(user=2)
            else:
                self.logged_in = True
                self._home()
        else:
            self._login(user=user)

    def _home(self):
        self._clear_terminal()
        if self.logged_in:
            print(f"{figlet_format('Dice Game')}")
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
        else:
            self._login()

    def _main_game(self):
        self._clear_terminal()
        print(f"{figlet_format('Dice Game')}")
        print("Player 1 press enter to roll dice")
        play = input()
        dice = (random.randint(1,7), random.randint(1,7))
        print(f"\u250c\u2500\u2500\u2500\u2510 \u250c\u2500\u2500\u2500\u2510 \n\u2502 {dice[0]} \u2502 \u2502 {dice[1]} \u2502\n\u2514\u2500\u2500\u2500\u2518 \u2514\u2500\u2500\u2500\u2518")

    def _leaderboard(self):
        self._clear_terminal()
        print(f"{figlet_format('Leaderboard')}")
        scores = []
        with open("./Dice-Game/leaderboard.txt") as f:
            for i in f:
               scores.append((i.split(':')[0].title(), i.split(':')[1].replace("\n", "")))
        scores = sorted(scores, key=lambda tup: int(tup[1]))
        for i in scores[:5]:
            print(f"{scores.index(i)+1}. {i[0]} - {i[1]}")
        back = input("Enter to go back")
        self._home()

    def run(self):
        self._login()

if __name__ == "__main__":
    dice_game().run()
