from ai import AI
from human import Human


class Game(AI,Human):
    def __init__(self):
        self.players = int
        self.welcome = ''
        super().__init__()


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
        
    def run_game(self):
        if self.player_one.choice_made_human():
            pass        
