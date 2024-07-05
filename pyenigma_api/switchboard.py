"""This module contains the implmentation for switch board"""

from typing import Dict, Tuple


class SwitchBoard:
    def __init__(self):
        """Class that implements the switch board

        Switchboard switches one character to the other depending upon
        whether there is a short present between the two characters. A short
        maps one character to the other and vice versa.
        Eg: A short between 'a'(1) and 'x'(24) will make an input of 'x'(24) to 'a'(1) and an
        input of 'a'(1) to  'x'(24).

        There can not be more than one short from any one of the characters as that
        would lead to non-determinism of the output.

        Attributes:
            shorts_dict (dict): Dictionary of all the short present in the switchboard.
                For every short there are two key value pairs present in the switchboard.
        """
        self._shorts_dict: Dict[int, int] = {}

    def add_short(self, short_tuple: Tuple[int, int]) -> None:
        """Add the provided short to the switchboard

        Args:
            short_tuple (tuple): The tuple of elements to be shorted.

        Raises:
            KeyError : Riases if the short is already present.
        """
        short_a, short_b = short_tuple
        if short_a in self._shorts_dict or short_b in self._shorts_dict:
            raise KeyError("The provided element is already shorted to another element")
        if short_a == short_b:
            raise Exception("An element cannot be shorted with itelf")
        self._shorts_dict[short_a] = short_b
        self._shorts_dict[short_b] = short_a

    def remove_short(self, short_tuple: Tuple[int, int]) -> None:
        """Remove the provided short from the switchboard

        Args:
            short_tuple (tuple): The tuple of short elements to be removed.

        Raise:
            KeyError : If the provided short is not present already in the
                switchboard

        """
        short_a, short_b = short_tuple
        if short_a not in self._shorts_dict or short_b not in self._shorts_dict:
            raise KeyError("The provided short is not present in the switch board")

    def get_output(self, input: int) -> int:
        """Get a output from the switchboad according to the shorts present"""
        if input in self._shorts_dict:
            return self._shorts_dict[input]
        return input


def module_demo() -> None:
    switch_board = SwitchBoard()
    switch_board.add_short((1, 3))
    switch_board.add_short((24, 25))
    print(switch_board.get_output(3))
    print(switch_board.get_output(1))
    print(switch_board.get_output(24))
    print(switch_board.get_output(25))
    print(switch_board.get_output(16))


if __name__ == "__main__":
    module_demo()
