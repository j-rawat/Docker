from config import Config
from zeep import client

import logging


class EnvironmentResolver:

    def __init__(self, endpoint):
        # self.headers = {
        #     "Accept-Encoding": "gzip,deflate",
        #     "Content-Type": "text/xml;charset=UTF-8",
        #     "SOAPAction": "\"http://roche.com/imageAnalysis/GetAlgorithmInformation\"",
        #     "Connection": "Keep-Alive"
        # }
        self.endpoint = endpoint

    # def GetAlgorithmInformation(self):
    def get_endpoint_info(self):
        return self.endpoint
