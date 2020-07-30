import pytest
import logging


@pytest.mark.sanity
def test_method11():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.regression
def test_method12():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.regression
def test_method13():
    logging.info('This is first step')
    assert 2 == 2
