
from player import Player

class Human(Player):
    def __init__(self):
        self.choice = ''
        super().__init__()

    def choice_made_human(self):
        gesture = False
        while gesture is False:
            selected_gesture = int(input('0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for spock'))
            if selected_gesture == 0:
                selected_gesture = self.gestures[0]
                gesture is True
                return selected_gesture
            elif selected_gesture == 1:
                selected_gesture = self.gestures[1]
                gesture = True
                return selected_gesture
            elif selected_gesture == 2:
                selected_gesture = self.gestures[2]
                gesture = True
                return selected_gesture
            elif selected_gesture == 3:
                selected_gesture = self.gestures[3]
                gesture = True
                return selected_gesture
            elif selected_gesture == 4:
                selected_gesture = self.gestures[4]
                gesture = True
                return selected_gesture
            else:
                print('Thats not a option, try again!')
      
    
        