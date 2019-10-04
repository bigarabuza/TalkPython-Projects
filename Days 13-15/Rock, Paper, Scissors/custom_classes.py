from random import choice

class Player:
    def __init__(self, name):
        self.name = name

class Roll:
    def __init__(self, name=None):
        self.rules = {
            'rock': ('paper', 'scissors'),
            'paper': ('scissors', 'rock'), 
            'scissors': ('rock', 'paper'),
    }
        if not name:
            self.name = choice(list(self.rules.keys()))
        else:
            self.name = name
        
    def can_defeat(self, other):
        try:
            if self.rules[self.name][1] == other:
                return 'win'
            elif self.name == other:
                return 'tie'
            else:
                return 'lose'
        except KeyError:
            return 'Please enter valid roll'
        

print(Roll('rock').can_defeat('rock'))

