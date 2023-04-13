#
# Purpur Tentakel
# Cooking Book
# 12.04.2023
#

from tests import test_helper as t_h


def test_generate_database() -> None:
    t_h.generate_temporary_database()
    t_h.delete_temporary_database()
