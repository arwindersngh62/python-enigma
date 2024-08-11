
from contextlib import nullcontext as does_not_raise # checkout pytest 
from pytest import fixture, mark, raises
from pyenigma_api.plugboard import PlugBoard

@fixture
def empty_plugboard():
    empty_plugboard = PlugBoard()
    return empty_plugboard 


@mark.parametrize(
    "short_tuple, shorts_dict",
    (((1,4), {1:4, 4:1}),
    ((2,6), {2:6, 6:2}),
    ((4,21), {4:21, 21:4}),
    ((12,19), {12:19, 19:12}),
    ((15,24), {15:24, 24:15}),
    ((19,1), {19:1, 1:19}),
    ((12,4), {12:4, 4:12}),
    ),
)
def test_plugboardbaord_add(empty_plugboard, short_tuple, shorts_dict):
    empty_plugboard.add_short(short_tuple)
    assert shorts_dict == empty_plugboard.shorts_dict

def test_plugboard_add_error_on_same_int(empty_plugboard):
    with raises(Exception, match = "An element cannot be shorted with itelf"):
        empty_plugboard.add_short((1,1))

@mark.parametrize(
    "short_added, present_shorts",
    (
        ((1,2), ((1,4),(3,2),(2,6),(1,6))),
        ((2,8), ((2,9),(8,21),(4,8),(19,2))),
    )
        
)
def test_plugboard_add_error_on_short_already_present(empty_plugboard, short_added, present_shorts):
    empty_plugboard.add_short(short_added)
    for repeating_short in present_shorts:
        with raises(KeyError, match = "The provided element is already shorted to another element"):
            empty_plugboard.add_short(repeating_short)
            
@mark.parametrize(
    "short, invalid_int, should_raise", 
    (
        ((0,2), 0, True),
        ((23,27), 27, True),
        ((0,80), 0, True),
        ((1,19), None, False),
    ),
)
def test_plugboard_short_not_alphabet(empty_plugboard, short, invalid_int, should_raise):
    if should_raise:
        with raises(KeyError, match = f"The provided short is not an alphabet: {invalid_int}"):
            empty_plugboard.add_short(short)
    else:
        with does_not_raise(): # It is just an empty context to ensure no errors are raised
            empty_plugboard.add_short(short)

def test_plugboard_remove_short():
    

def test_plugboard_ouput():
    pass