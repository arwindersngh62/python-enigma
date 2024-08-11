"""This module contains the implmentation for plugboard"""
import functools
from typing import Dict, Tuple, List


#TODO :  Fix the error types to proper types

def ensure_short_is_alphabet(func):
    """Ensuring that supplied short ints are between 1-27"""
    @functools.wraps(func)
    def wrapper_ensure_alphabet(*args, **kwargs):
        try:
            input_shorts = args[1]
        except:
            input_shorts = kwargs["short_tuple"]
            
        for short_int in input_shorts:
            if short_int > 26 or short_int<1:
                raise KeyError(f"The provided short is not an alphabet: {short_int}")
        func(*args, **kwargs)

    return wrapper_ensure_alphabet


class PlugBoard:
    """Class that implements the plugboard

    Plugboard switches one character to the other depending upon
    whether there is a shorting cable(short) present between the two characters. A short
    maps one character to the other and vice versa.
    Eg: A short between 'a'(1) and 'x'(24) will make an input of 'x'(24) to 'a'(1) and an
    input of 'a'(1) to  'x'(24).
    There cannot be more than one shorts to or from any one of the characters as that
    would lead to non-determinism of the output. 

    Attributes:
        shorts_dict (dict): Dictionary of all the short present in the plugboard.
            For every short there are two key value pairs present in the plugboard.
        shorts (dict): List of all the short tuples in the plugboard.
    """
    def __init__(self):
        """Initialize the plugboard with new shorts"""
        self.shorts_dict: Dict[int, int] = {}
        self.shorts_list: List[Tuple[int, int]] = []
    
    @ensure_short_is_alphabet
    def add_short(self, short_tuple: Tuple[int, int]) -> None:
        """Add the provided short to the plugboard

        Args:
            short_tuple (tuple): The tuple of elements to be shorted.

        Raises:
            KeyError : Riases if the short is already present.
        """
        short_a, short_b = short_tuple
        if short_a in self.shorts_dict or short_b in self.shorts_dict:
            raise KeyError("The provided element is already shorted to another element")
        if short_a == short_b:
            raise Exception("An element cannot be shorted with itelf")
        self.shorts_dict[short_a] = short_b
        self.shorts_dict[short_b] = short_a
        self.shorts_list.append(short_tuple)

    @ensure_short_is_alphabet
    def remove_short(self, short_tuple: Tuple[int, int]) -> None:
        """Remove the provided short from the plugboard

        Args:
            short_tuple (tuple): The tuple of short elements to be removed.

        Raise:
            KeyError : If the provided short is not present already in the
                plugboard

        """
        short_a, short_b = short_tuple
        if short_a not in self.shorts_dict or short_b not in self.shorts_dict:
            raise KeyError("The provided short is not present in the switch board")
        self.shorts_dict.pop(short_a)
        self.shorts_dict.pop(short_b)
        self.shorts_list.remove(short_tuple)


    def get_output(self, input_int: int) -> int:
        """Get a output from the switchboad according to the shorts present"""
        if input_int > 26 or input_int < 1:
            raise KeyError(f"The provided short is not an alphabet: {input_int}")
        if input_int in self.shorts_dict:
            return self.shorts_dict[input_int]
        return input_int


def module_demo() -> None:
    switch_board = PlugBoard()
    switch_board.add_short((15, 3))
    switch_board.add_short((24, 25))
    print(switch_board.get_output(in_int= 3))
    print(switch_board.get_output(1))
    print(switch_board.get_output(24))
    print(switch_board.get_output(25))
    print(switch_board.get_output(4))


if __name__ == "__main__":
    module_demo()
