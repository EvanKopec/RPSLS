from player import Player

class Human(Player):
    def __init__(self):
        self.choice_made = ''
        super().__init__()

    def choice_made(self):
        choice = input('Choose 0 for Rock, 1 for Papaer, 2 for Scissors, 3 Lizard, 4 Spock')
        while choice == ['0', '1', '2', '3', '4']:
            print(choice)
        else:
            print('Thats not a option, try again.')
    
        