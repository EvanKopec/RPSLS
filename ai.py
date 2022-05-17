from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()


    def choice_made(self):
        gesture = False
        while gesture is False:
            selected_gesture = (random.choice(self.gestures))
            if selected_gesture == 'Rock':
                self.selected_gesture = self.gestures[0]
                gesture = True
                print(f'You selected {self.selected_gesture}!')
            elif selected_gesture == 'Paper':
                self.selected_gesture = self.gestures[1]
                gesture = True
                print(f'You selected {self.selected_gesture}!')
            elif selected_gesture == 'Scissors':
                self.selected_gesture = self.gestures[2]
                gesture = True
                print(f'You selected {self.selected_gesture}!')
            elif selected_gesture == 'Lizard':
                self.selected_gesture = self.gestures[3]
                gesture = True
                print(f'You selected {self.selected_gesture}!')
            elif selected_gesture == 'Spock':
                self.selected_gesture = self.gestures[4]
                gesture = True
                print(f'You selected {self.selected_gesture}!')
            else:
                print('Thats not a option, try again!')