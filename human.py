
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def choice_made(self):
        gesture = False
        while gesture is False:
            selected_gesture = int(input('0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for spock'))
            if selected_gesture == 0:
                self.selected_gesture = self.gestures[0]
                gesture = True
                print(self.selected_gesture)
            elif selected_gesture == 1:
                self.selected_gesture = self.gestures[1]
                gesture = True
            elif selected_gesture == 2:
                self.selected_gesture = self.gestures[2]
                gesture = True
                print(self.selected_gesture)
            elif selected_gesture == 3:
                self.selected_gesture = self.gestures[3]
                gesture = True
            elif selected_gesture == 4:
                self.selected_gesture = self.gestures[4]
                gesture = True
            else:
                print('Thats not a option, try again!')
      
    
        