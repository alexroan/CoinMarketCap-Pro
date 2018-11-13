class EndpointType:

    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

class Cryptocurrency(EndpointType):
    __ENDPOINT = '/v1/cryptocurrency'

    def info(self, id='', symbol=''):
        return self.url + self.__ENDPOINT + '/info'

class Exchange:
    __ENDPOINT = '/v1/exchange'

class GlobalMetrics:
    __ENDPOINT = '/v1/global-metrics'

class Tools:
    __ENDPOINT = '/v1/tools'