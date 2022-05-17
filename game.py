from ai import AI
from human import Human
from player import Player


class Game(AI,Human):
    def __init__(self):
        self.players = int
        self.welcome = ''
        super().__init__()

    def run_game(self):
        self.display_welcome()
        self.how_many_players()
        self.round()

    def display_welcome(self):
        print('Welcome')
        print('Game Rules:')
        print('Rock crushes Scissors')
        print('Scissors cuts Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaportizes Rock')

    def how_many_players(self):
        user_input = int(input('How many players? Enter 1 for single player, Enter 2 for multiplayer:'))
        if user_input == 1:
            self.player_one = Human()
            self.player_two = AI()
        elif user_input == 2:
            self.player_one = Human()
            self.player_two = Human()

    def player_turns(self):
        pass

        
    def round(self):
        
        while self.player_one.wins < 2 and self.player_two.wins < 2:
            self.player_one.choice_made()
            self.player_two.choice_made()
            if self.player_one.selected_gesture == self.player_one.gestures[0] and self.player_two.selected_gesture == self.player_two.gestures[2]:
                self.player_one.wins += 1
                print('Player One wins the round')
            else:
                print('Broken')


        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 2 and self.player_two.choice_made() == 1:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 2 and self.player_one.choice_made == 1:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 1 and self.player_two.choice_made() == 0:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')
        #  if self.player_one.choice_made() == 0 and self.player_two.choice_made() == 2:
        #     self.player_one.wins += 1
        #     print('Player One wins the round')
        #  elif self.player_two.choice_made() == 0 and self.player_one.choice_made == 2:
        #     self.player_two.wins += 1
        #     print('Player Two wins!')

                    
