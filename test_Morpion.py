from Morpion import *

def test_has_win_win():
    tabtest=([":)"," "," "], [":)", " ", " "], [":)", " ", " "])
    assert has_win(tabtest)

def test_has_not_win():
    tabtest=([":)"," "," "], [":("," "," "], [":)"," "," "])
    assert not has_win(tabtest)
