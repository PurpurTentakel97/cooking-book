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
