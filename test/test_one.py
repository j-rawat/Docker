import pytest
import logging


@pytest.mark.smoke
def test_method1():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.smoke
def test_method2():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.e2e
def test_method3():
    logging.info('This is first step')
    assert 2 == 2
