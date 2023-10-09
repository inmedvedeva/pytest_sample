from main import check_list
import pytest


@pytest.fixture
def text_for_pass():
    return 'Hello it is test name'


@pytest.fixture
def text_for_fail():
    return 'Hello or it is test name'


def test_get_pass(text_for_pass):
    res = check_list(text_for_pass)
    assert res == "PASS"


def test_get_fail(text_for_fail):
    res = check_list(text_for_fail)
    assert res == 'FAIL'
