from pytest import fixture
from .config import Config

import os
import sys
from _pytest.runner import runtestprotocol


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment for Upath"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


