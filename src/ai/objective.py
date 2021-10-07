from model.state import State

class Objective:
    def __init__(self, _state):
        self.state = _state

    
        
    def value(self, player : int) -> int:
        """
        player : player who is playing right now
        """
