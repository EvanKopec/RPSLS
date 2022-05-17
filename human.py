import re
from player import Player

class Human(Player):
    def __init__(self):
        self.choice = ''
        super().__init__()

    def choice_made(self):

        gesture = False
        while gesture is False:
            user_input = int(input('0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for spock'))
            if user_input == 0:
                user_input = self.gestures[0]
                gesture is True
                return user_input
            elif user_input == 1:
                user_input = self.gestures[1]
                gesture = True
                return user_input
            elif user_input == 2:
                user_input = self.gestures[2]
                gesture = True
                return user_input
            elif user_input == 3:
                user_input = self.gestures[3]
                gesture = True
                return user_input
            elif user_input == 4:
                user_input = self.gestures[4]
                gesture = True
                return user_input
            else:
                print('Thats not a option, try again!')
      
    
        