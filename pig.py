import random
random.seed(0)
class Player:
    def __init__(self, id):
        self.id = id
        self.score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def hold(self, temp_score):
        self.score += temp_score
        print(f"\nPlayer {self.id} holds. Current score: {self.score}")

    def check(self):
        if self.score >= 100:
            return True

class PigGame:
    def __init__(self):
        self.players = [Player(1), Player(2)]
        self.current_player = 0
        self.temp_score = 0

    def switch_player(self):
        self.current_player = (self.current_player + 1) % 2 
        self.temp_score = 0

    def start(self):
        while True:
            print(f"\nPlayer {self.players[self.current_player].id}'s Current Score: {self.players[self.current_player].score}")
            choice = input("Enter 'r' to roll the dice or 'h' to hold: ")

            if choice == 'r':
                dice_roll = self.players[self.current_player].roll_dice()
                print(f"\nPlayer {self.players[self.current_player].id} rolled a {dice_roll}")

                if dice_roll == 1:
                    print("A 1 was rolled. Temp score reset to 0.")
                    self.switch_player()
                else:
                    self.temp_score += dice_roll
                    print(f"Temp score: +{self.temp_score} Temp total: {self.players[self.current_player].score + self.temp_score}")

            elif choice == 'h':
                self.players[self.current_player].hold(self.temp_score)

                if self.players[self.current_player].check():
                    print(f"\nPlayer {self.players[self.current_player].id} wins!")
                    break

                self.switch_player()

            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    game = PigGame()
    game.start()
