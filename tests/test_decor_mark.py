import pytest


@pytest.mark.smoke #в терминале: pytest tests/test_decor_mark.py -m smoke
def test_mark_1():
    assert True


@pytest.mark.regress #в терминале: pytest tests/test_decor_mark.py -m regress
def test_mark_2():
    assert True


@pytest.mark.regress
def test_mark_3():
    assert True


@pytest.mark.regress
def test_mark_4():
    assert True