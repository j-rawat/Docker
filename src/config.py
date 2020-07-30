class Config:

    def __init__(self, env):
     self.env = env
     self.endpoint = {
            'qa': 'http://10.20.85.208//uPath-services/ConnectVToVirtuosoWebService/ConnectVToVirtuosoWebServiceImpl?wsdl',
            'integration' :'http://10.20.85.208//uPath-services/ConnectVToVirtuosoWebService/ConnectVToVirtuosoWebServiceImpl?wsdl_INTEGRATIONqa',
            'prod' : 'http://10.20.85.208//uPath-services/ConnectVToVirtuosoWebService/ConnectVToVirtuosoWebServiceImpl?wsdl_prod',
     } [env]


