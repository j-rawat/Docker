import pytest
import logging


@pytest.mark.sanity
def test_method1(get_wsdl, setup):
    print(get_wsdl)
    assert 2 == 2

@pytest.mark.sanity
def test_method2(helper):
    print(helper.testme())
    logging.info('I am reading XML')
    payload = helper.getPayload('addcase.xml', 'accessionNumber', 'blockBarcode', 'labelId', 'specimenBarcode')
    print(payload)
    accessionNumber = helper.get_tag_text(payload, 'accessionNumber')
    print(accessionNumber)

@pytest.mark.regression
def test_method3():
    logging.info('This is first step')
    assert 2 == 2
