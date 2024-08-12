
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

@mark.parametrize(
    "present_shorts, remove_short, expected_shorts_list, expected_shorts_dict",
    (
        (((1,5),(7,2),(9,10),(19,21)),(19,21), [{1,5},{7,2},{9,10}], {1:5, 5:1, 7:2, 2:7, 9:10 , 10:9}),
        (((2,4), (10,11), (15,17), (23,24)),(24,23), [{2,4},{10,11},{15,17}], {2:4, 4:2, 10:11, 11:10, 15:17 , 17:15}),
        
 #       (((1,4), (17,11), (14,19), (20,24)),(24,20), [(1,4),(17,11),(15,17)], {2:4, 4:2, 10:11, 11:10, 15:17 , 17:15}),
  #      (((20,9), (10,11), (15,17), (23,24)),(23,24), [(2,4),(10,11),(15,17)], {2:4, 4:2, 10:11, 11:10, 15:17 , 17:15}),
   #     (((10,7), (10,11), (15,17), (23,24)),(23,24), [(2,4),(10,11),(15,17)], {2:4, 4:2, 10:11, 11:10, 15:17 , 17:15}),
    )
)
def test_plugboard_remove_short(empty_plugboard, present_shorts, remove_short, expected_shorts_list, expected_shorts_dict):
    for short in present_shorts:
        empty_plugboard.add_short(short)
    empty_plugboard.remove_short(remove_short)
    assert expected_shorts_dict == empty_plugboard.shorts_dict
    assert expected_shorts_list == empty_plugboard.shorts_list
       

def test_plugboard_ouput():
    pass