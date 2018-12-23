from itertools import islice

import pytest


@pytest.fixture(autouse=True)
def add_np(doctest_namespace):
    doctest_namespace["islice"] = islice
