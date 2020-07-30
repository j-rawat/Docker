import pytest
import logging


@pytest.mark.sanity
def test_method1():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.sanity
def test_method2():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.regression
def test_method3():
    logging.info('This is first step')
    assert 2 == 2
