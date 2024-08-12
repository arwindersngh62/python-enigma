from typing import Tuple, List 

from pyenigma_api.plugboard import PlugBoard


class EngimaInterface:
    
    
    def __init__(self, plugboard: PlugBoard):
        self.plugboard = plugboard
    
        
    

# This architecture defines the whole enigma machine as one service.
plugboard = PlugBoard()     
enigma = EngimaInterface(plugboard)