#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

import pytest

from validation import v_helper as v_h
from helper import return_message as r_m


@pytest.mark.parametrize(("ID", "expected"), [
    # @formatter:off
    (1,       True ),  # positive int
    (-5,      False),  # negative int
    (0,       False),  # 0 int
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
    (3.5,     True ),  # positive float
    (-3.6,    False),  # negative float
    (0.0,     False),  # 0.0 float
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


@pytest.mark.parametrize(("value", "expected"), [
    # @formatter:off
    ("test",      True),  # string with entry
    ("Test",      True),  # caps
    ("    test",  True),  # white space in front
    ("test     ", True),  # white space in back
    ("     ", False),  # only white space
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
    ("test",      True),  # string with entry
    ("Test",      True),  # caps
    ("    test",  True),  # white space in front
    ("test     ", True),  # white space in back
    ("     ",     True),  # only white space
    ("",          True),  # empty string
    (str(),       True),  # string ctor
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
    (r_m.ReturnMessage(    True ), True ),  # return message without value
    (r_m.ReturnMessage(    False), False),  # return message without value
    (r_m.ReturnMessageNone(True ), True ),  # return message without value
    (r_m.ReturnMessageNone(False), False),  # return message without value
    (r_m.ReturnMessageStr(  "",   True ), True ),  # return message with value
    (r_m.ReturnMessageStr(  "",   False), False),  # return message with value
    (r_m.ReturnMessageInt(   0,   True ), True ),  # return message with value
    (r_m.ReturnMessageInt(   0,   False), False),  # return message with value
    (r_m.ReturnMessageTuple((0,), True ), True ),  # return message with value
    (r_m.ReturnMessageTuple((0,), False), False),  # return message with value
    (r_m.ReturnMessageList( [0],  True ), True ),  # return message with value
    (r_m.ReturnMessageList( [0],  False), False),  # return message with value
    # @formatter:on
])
def test_is_valid_return_message(message, expected) -> None:
    result = v_h.is_valid_Return_Message(message)
    assert result == expected
