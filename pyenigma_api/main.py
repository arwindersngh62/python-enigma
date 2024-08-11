from typing import Tuple, List 

from pyenigma_api.plugboard import SwitchBoard


class EngimaInterface:
    
    
    def __init__(self, switchboard: SwitchBoard):
        self.switchboard = switchboard
    
    @property
    def switchboard_shorts(self)-> List[Tuple[int, int]]:
        return self.switchboard.shorts_list
    
    @switchboard_shorts.setter
    def switchboard_shorts(self, shorts_list: List[Tuple[int, int]]):
        for short in shorts_list:
            self.switchboard.add_short(short)
    
    def add_switchboard_short(self, short_tuple):
        self.switchboard.add_short(short_tuple)


switchboard = SwitchBoard()     
enigma = EngimaInterface(switchboard)