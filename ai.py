from player import Player
import random

class AI(Player):
    def __init__(self):
        self.choice = ''
        super().__init__()


    def choice_made_ai(self):
        gesture = False
        while gesture is False:
            ai_input = (random.choice(self.gestures))
            if ai_input == 'Rock':
                ai_input = self.gestures[0]
                gesture is True
                return ai_input
            elif ai_input == 'Paper':
                ai_input = self.gestures[1]
                gesture = True
                return ai_input
            elif ai_input == 'Scissors':
                ai_input = self.gestures[2]
                gesture = True
                return ai_input
            elif ai_input == 'Lizard':
                ai_input = self.gestures[3]
                gesture = True
                return ai_input
            elif ai_input == 'Spock':
                ai_input = self.gestures[4]
                gesture = True
                return ai_input
            else:
                print('Thats not a option, try again!')