import sys
import random
import string
import allure
import pytest


# Printing unique id using uuid1()
def get_unique():
    unique = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))
    return unique

