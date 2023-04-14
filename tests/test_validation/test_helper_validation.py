#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from validation import v_helper as v_h
from helper import return_message as r_m


# @formatter:off
@pytest.mark.parametrize(("ID", "expected"), [
    (1,       True ),
    (-5,      False),  # ID to low
    (0,       False),  # ID is zero
    (bool(),  False),  # wrong datatype
    (str(),   False),  # wrong datatype
    (float(), False),  # wrong datatype
    (list(),  False),  # wrong datatype
    (tuple(), False),  # wrong datatype
    (dict(),  False),  # wrong datatype
    (type,    False),  # wrong datatype
# @formatter:on
])
def test_is_valid_ID(ID, expected) -> None:
    result = v_h.is_valid_ID(ID)
    assert result == expected


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    (0.0,     True ),
    (3.5,     True ),
    (-3.6,    False),  # negative number
    (bool(),  False),  # wrong datatype
    (str(),   False),  # wrong datatype
    (int(),   False),  # wrong datatype
    (list(),  False),  # wrong datatype
    (tuple(), False),  # wrong datatype
    (dict(),  False),  # wrong datatype
    (type,    False),  # wrong datatype
    # @formatter:on
])
def test_is_valid_positive_float(value, expected) -> None:
    result = v_h.is_valid_positive_float(value)
    assert result == expected


# @formatter:off
@pytest.mark.parametrize(("value", "expected"), [
    ("test",      True),
    ("Test",      True),
    ("    test",  True),
    ("test     ", True),
    ("     ", False),  # empty string
    ("",      False),  # empty string
    (bool(),  False),  # wrong datatype
    (str(),   False),  # wrong datatype
    (int(),   False),  # wrong datatype
    (float(), False),  # wrong datatype
    (list(),  False),  # wrong datatype
    (tuple(), False),  # wrong datatype
    (dict(),  False),  # wrong datatype
    (type,    False),  # wrong datatype
# @formatter:on
])
def test_is_valid_string(value, expected) -> None:
    result = v_h.is_valid_string(value)
    assert result == expected


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("test",      True),
    ("Test",      True),
    ("    test",  True),
    ("test     ", True),
    ("     ",     True),
    ("",          True),
    (str(),       True),
    (bool(),  False),  # wrong datatype
    (int(),   False),  # wrong datatype
    (float(), False),  # wrong datatype
    (list(),  False),  # wrong datatype
    (tuple(), False),  # wrong datatype
    (dict(),  False),  # wrong datatype
    (type,    False),  # wrong datatype
    # @formatter:on
])
def test_is_valid_empty_string(value, expected) -> None:
    result = v_h.is_valid_empty_string(value)
    assert result == expected


@pytest.mark.parametrize(("message", "expected"), [
    # @formatter:off
    (r_m.ReturnMessage(    True ), True ),
    (r_m.ReturnMessage(    False), False),
    (r_m.ReturnMessageNone(True ), True ),
    (r_m.ReturnMessageNone(False), False),
    (r_m.ReturnMessageStr(  "",   True ), True ),
    (r_m.ReturnMessageStr(  "",   False), False),
    (r_m.ReturnMessageInt(   0,   True ), True ),
    (r_m.ReturnMessageInt(   0,   False), False),
    (r_m.ReturnMessageTuple((0,), True ), True ),
    (r_m.ReturnMessageTuple((0,), False), False),
    (r_m.ReturnMessageList( [0],  True ), True ),
    (r_m.ReturnMessageList( [0],  False), False),
    # @formatter:on
])
def test_is_valid_return_message(message, expected) -> None:
    result = v_h.is_valid_Return_Message(message)
    assert result == expected
