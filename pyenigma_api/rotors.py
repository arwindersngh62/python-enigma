"""This module contains the implementation of rotors and reflector"""

@staticmethod
def shift_string_left(string_in: str, shift_count:int):
    return string_in[shift_count:] + string_in[:shift_count]

class Rotor:
    """The class implementing the rotor
    
    A rotor has a wiring connecting a character from one side to another 
    character on the other side. There is a notch that decides when the next
    rotor will rotate with the current one. The ring setting changes the alphabet ring
    which means it shifts entire mapping of alphabet ring.
    We are assuming a fixed distance between notch and the window, which is two thirds of
    the alphabets which is 18. This means if the notch is at 'a' and we start from there
    we will have change on next rotor after 18 rotations.
    
    Attributes:
        base_wiring (str): A string of 26 characters that represents the base wiring
        notch (str): The place of the notch on the alphabet ring 
        ring_setting (str): The char representing how much alphabet ring is shifted
            from 
    """
    notch_distance = 18
    
    def __init__(self):
        """
        The Rotor class creates objects that represent a rotor in enigma machine
        a rotor gets an input and converts it into a different character.
        The inside of a rotor is wires mapping one contact on one side to a
        different contact on the other side.
        The constructor requires a rotor type which should be a key for the
        rotor types dictionary given above.
        """
        self.base_wiring = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
        self.notch = "A"
        self.ring_setting = "A"
        self.actual_wiring = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
        
        
        # TODO checks are needed for entire config:
        # TODO length checks
        # TODO base_wiring check for repetition
        
        
    def apply_entire_config(self, base_wiring:str, notch:str, ring_setting:str):
        self.base_wiring = base_wiring
        self.notch = notch
        self.ring_setting = ring_setting
        
        # Apply the ring setting to the base setting
        rotate_base_by = ord(ring_setting) - 65
        self.actual_wiring = shift_string_left(self.base_wiring, rotate_base_by)
        

    def get_output(self, in_int: int) -> int:
        """
        The method that converts the input to the output across the rotor
        it simple means the getting the character from the rotor type string
        based on the int position of input character.
        """
        # The in_input is indexed from 1 but the list is indexed from 0
        return ord(self.actual_wiring[in_int-1]) - 64

    def get_rev_output(self, in_int: int) -> int:
        """
        the method is same it gets the output from the other side.
        this is done by finding where the char being inpput is present
        on the string of rotor type and return its index.
        """
        return self.actual_wiring.index(chr(in_int + 64)) + 1

def module_demo():
    rotor = Rotor()
    rotor.apply_entire_config(base_wiring = "EKMFLGDQVZNTOWYHXUSPAIBRCJ", notch = "A", ring_setting = "B")
    print(rotor.get_output(1))
    print(rotor.get_rev_output(11))
    
if __name__ == "__main__":
    module_demo()
