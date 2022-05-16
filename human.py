from player import Player

class Human(Player):
    def __init__(self):
        self.choice = ''
        super().__init__()

    def choice_made(self):
        user_input = int(input('0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for spock'))
        gesture = False
        while gesture is False:
            if user_input == 0:
                user_input = self.gestures[0]
                gesture is True
      
    
        