import pytest
from .utils.resolver import EnvironmentResolver
from .utils.helper import Helper
import logging
import allure


@pytest.fixture()
def helper():
    helper = Helper()
    return helper


@pytest.fixture(scope="function")
def endpointExtractor(app_config):
    endpoint = EnvironmentResolver(app_config.endpoint)
    return endpoint


@pytest.fixture(scope='function')
def get_wsdl(endpointExtractor):
    endpoint = endpointExtractor.get_endpoint_info()
    return endpoint


@pytest.fixture()
def setup(request):
    print("********************************" + request.node.name + " started running ********************************")
    yield
    print("********************************" + request.node.name + " completed running *******************************")


# @pytest.fixture(scope="function")
# def tc_logger(request):
#     # logger_for_classes = logging.getLogger('smoke.Classes')  # TODO: fix to relative path
#     logger_for_testcases = logging.getLogger(request.function.__name__)
#     # logger_for_classes.setLevel(logging.INFO)
#     logger_for_testcases.setLevel(logging.INFO)
#
#     # create file handler
#     handler = logging.FileHandler('./Logs/TestCaseLogs/{}.log'.format(request.function.__name__), 'w+')
#     handler.setLevel(logging.INFO)
#
#     # create a logging format
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     handler.setFormatter(formatter)
#
#     # add the file handler to the logger
#     # logger_for_classes.addHandler(handler)
#     logger_for_testcases.addHandler(handler)
#     yield logger_for_testcases
#     handler.close()
#     # logger_for_classes.removeHandler(handler)
#     logger_for_testcases.removeHandler(handler)


class AllureLoggingHandler(logging.Handler):
    def log(self, message):
        with allure.step('Log {}'.format(message)):
            pass

    def emit(self, record):
        self.log("({}) {}".format(record.levelname, record.getMessage()))


class AllureCatchLogs:
    def __init__(self):
        self.rootlogger = logging.getLogger()
        self.allurehandler = AllureLoggingHandler()

    def __enter__(self):
        if self.allurehandler not in self.rootlogger.handlers:
            self.rootlogger.addHandler(self.allurehandler)

    def __exit__(self, exc_type, exc_value, traceback):
        self.rootlogger.removeHandler(self.allurehandler)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call():
    with AllureCatchLogs():
        yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown():
    with AllureCatchLogs():
        yield
