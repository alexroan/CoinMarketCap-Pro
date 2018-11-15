class EndpointType:

    def __init__(self, requester):
        self.requester = requester

    def construct_params(self, key, value):
        params = key + '='
        if isinstance(value, list):
            counter = 0
            while (counter < len(value)):
                if counter == (len(value) - 1):
                    params += str(value[counter])
                else:
                    params += str(value[counter]) + ','
                counter += 1
        else:
            params += str(value)
        return params



class Cryptocurrency(EndpointType):
    __ENDPOINT = '/v1/cryptocurrency'

    def info(self, id=None, symbol=None):
        if id == None and symbol == None:
            raise Exception('Needs at least one of id or symbol')

        params = ''
        if id != None:
            params = self.construct_params('id', id)
        elif symbol != None:
            params = self.construct_params('symbol', symbol)

        endpoint = self.__ENDPOINT + '/info'
        return self.requester.request(endpoint, params)

class Exchange:
    __ENDPOINT = '/v1/exchange'

class GlobalMetrics:
    __ENDPOINT = '/v1/global-metrics'

class Tools:
    __ENDPOINT = '/v1/tools'