# import pytest
# import logging
# from .tests.util.algorithms import EnvironmentResolver
# from .config import Config
# import os
# import sys
# # import time
# # import tesults
# # from _pytest.runner import runtestprotocol
# # from py.xml import html
# # from datetime import datetime
#
# @pytest.fixture(scope="module")
# def helper():
#     helper = Helper()
#     return helper
#
# @pytest.fixture(scope="function")
# #def algorithmInTest(app_config):
# def endpointExtractor(app_config):
#     endpoint = EnvironmentResolver(app_config.endpoint)
#     return endpoint
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         # always add url to report
#         extra.append(pytest_html.extras.url('http://www.example.com/'))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
#         report.extra = extra
#
#
# def pytest_html_report_title(report):
#    report.title = "UPATH - SOAP APIs Test Summary"
#
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_html_results_summary(prefix, summary, postfix):
# #     prefix.extend([html.p("foo: bar")])
# #     summary.extend([html('<div>Additional HTML</div>')])
#
# def pytest_configure(config):
#     config._metadata['customized'] = 'detail'
