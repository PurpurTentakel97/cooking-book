#
# Purpur Tentakel
# Cocking Book
# 12.04.2023
#
import pytest

from tests import test_helper as t_h
from database import add as a
from database import update as u
from database import database as d
from database import select as s


@pytest.mark.parametrize("expected", [
    [(1, "Frühstück"),
     (2, "Mittagessen"),
     (3, "Abendessen")]
])
def test_select_all_raw_types(expected):
    expected.sort(key=lambda x: x[1])
    t_h.generate_temporary_database()
    values = s.select.select_all_raw_types()

    assert values.valid

    for (p_id, p_value), (l_id, l_value) in zip(expected, values.entry):
        assert p_id == l_id
        assert p_value == l_value

    t_h.delete_temporary_database()