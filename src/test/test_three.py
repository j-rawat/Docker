
import logging
#from .utils import helper
import pytest



# @pytest.fixture(scope='function')
# def get_wsdl(endpointExtractor):
#     endpoint = endpointExtractor.get_endpoint_info()
#     return endpoint
#
#
# @pytest.fixture()
# def setup(request):
#     print("********************************" + request.node.name + " started running ********************************")
#     yield
#     print("********************************" + request.node.name + " completed running *******************************")


@pytest.mark.sanity
def test_readingXML(setup, helper):
    logging.info('I am reading XML')
    payload = helper.getPayload('addcase.xml', 'accessionNumber', 'blockBarcode', 'labelId', 'specimenBarcode')
    accessionNumber = helper.get_tag_text(payload, 'accessionNumber')
    print(accessionNumber)


@pytest.mark.regression
def test_method12():
    logging.info('This is first step')
    assert 2 == 2


@pytest.mark.regression
def test_method13():
    logging.info('This is first step')
    assert 2 == 2
