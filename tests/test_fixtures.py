#
# Purpur Tentakel
# Cooking Book
# 13.04.2023
#

import pytest
from tests import test_helper as t_h


@pytest.fixture
def database_fixture():
    t_h.generate_temporary_database()
    yield
    t_h.delete_temporary_database()


@pytest.fixture
def main_window_fixture():
    t_h.generate_temporary_database()
    t_h.generate_main_window()
    yield
    t_h.shut_down_UI()
    t_h.delete_temporary_database()
