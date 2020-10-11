import os
import random
import time

from pyfiglet import figlet_format


class dice_game():

    def __init__(self):
        self.ROUNDS = 5
        self.logged_in = False
        self.scores = {"p1": {"score": 0, "roll": 0}, "p2": {"score": 0, "roll": 0}}
        self.users = []
        with open("./Dice-Game/users.txt") as f:
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
            print("Incorrect Credentials")
            time.sleep(1.5)
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
        self._game_rounds() # Plays 5 rounds
        self.scores["p1"]["score"] = self.scores["p2"]["score"]
        if self.scores["p1"]["score"] == self.scores["p2"]["score"]: # If the scores are even it makes each user roll a dice till someone has th highest roll
            while self.scores["p1"]["roll"] == self.scores["p2"]["roll"]: # Makes each user roll until someone gets a higher number than the other
                self._clear_terminal()
                print(figlet_format("It's a Tie"))
                for i in range(1,3):
                    print(f"Player {i} press Enter to roll") # Player presses enter to roll
                    x = input()
                    self.scores[f"p{i}"]["roll"] = random.randint(1,6) # Rolls one dice
            winner = 1 if self.scores["p1"]["roll"] > self.scores["p2"]["roll"] else 2 # Winner is whoever has the highest roll
            loser = 1 if winner == 2 else 2 # Loser is whoever has the lowest roll
        else:
            winner = 1 if self.scores["p1"]["score"] > self.scores["p2"]["score"] else 2 # Winner is whoever has the lowest score
            loser = 1 if winner == 2 else 2 # Loser is whoever has the lowest score
        self._clear_terminal()
        print(figlet_format(f"Player {winner} Wins!")) # Displays winners
        print(f"Player {winner} Score: {self.scores[f'p{winner}']['score']}")
        print(f"Player {loser} Score: {self.scores[f'p{loser}']['score']}")
        leaderboard_name = input(f"Enter the name you would like on the leaderboard player {winner} - ")
        with open("./Dice-Game/leaderboard.txt", "a+") as f:
            f.write(f"\n{leaderboard_name}:{self.scores[f'p{winner}']['score']}")
        print("Added to leaderboard")
        print("Press enter to go back to menu")
        x = input()
        self._home()

    def _leaderboard(self):
        self._clear_terminal()
        print(f"{figlet_format('Leaderboard')}")
        scores = []
        with open("./Dice-Game/leaderboard.txt") as f: # Opens txt file
            for i in f:
               scores.append((i.split(':')[0].title(), i.split(':')[1].replace("\n", ""))) # Gets all the users form the txt file into a list
        scores = sorted(scores, key=lambda tup: int(tup[1]))[::-1] # Sorts list into highest to lowest
        for i in scores[:5]: # Cycles through the top five players in the list
            print(f"{scores.index(i)+1}. {i[0]} - {i[1]}") # Prints each player in leaderboard upto 5
        back = input("Enter to go back")
        self._home()

    def _game_rounds(self):
        def sub_round(player_number):
            self._clear_terminal() # Clears terminal
            print(f'{figlet_format(f"Player {player_number}s Turn")}')
            print(f"Player {player_number} press enter to roll dice")
            play = input() # Gets user to rolls dice
            dice = (random.randint(1,6), random.randint(1,6)) # Gets Dice Roll
            self.scores[f"p{player_number}"]["score"] += dice[0] + dice[1] # Adds it to player score
            print(f"You rolled {dice[0]} and {dice[1]}") # Prints score
            if dice[0]+dice[1] % 2 == 0: # Checks if the roll is even
                self.scores[f"p{player_number}"]["score"] += 10
                print("You rolled an even thats plus 10 points!")
            elif self.scores[f"p{player_number}"]["score"] > 4:
                self.scores[f"p{player_number}"]["score"] -= 5
                print("You rolled an odd thats minus 5 points!")

            if dice[0] == dice[1]: # Checks if its a double
                print("You rolled a double heres another roll")
                print("Press enter to roll dice")
                play = input()
                dice = random.randint(1,7)
                print(f"You rolled {dice}")
                self.scores[f"p{player_number}"]["score"] += dice
            print(f"Player {player_number} turn over")
            print("Press enter to continue")
            x = input()

        for i in range(0,5): # Plays 5 rounds
            for x in range(1,3): # Plays each player twice per round
                sub_round(x)
            self._clear_terminal()
            print(figlet_format("Scores So Far"))
            for i in range(1,3):
                print(f"Player {i} - {self.scores[f'p{i}']['score']}")
            print("Press enter to play the next round")
            x = input()

    def run(self):
        self._login()

if __name__ == "__main__":
    dice_game().run()
