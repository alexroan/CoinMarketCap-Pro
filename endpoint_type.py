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

    def __init__(self, requester):
        EndpointType.__init__(self, requester=requester)
        self.listings = Listings(requester=self.requester, base_endpoint=self.__ENDPOINT)

    # /info endpoint.
    def info(self, id=None, symbol=None):
        if id == None and symbol == None:
            raise Exception('Needs at least one of id or symbol')
        if id != None and symbol != None:
            raise Exception('Either id or symbol, not both')

        params = self.construct_params('id', id) if id != None else None
        if params == None:
            params = self.construct_params('symbol', symbol) if symbol != None else None

        endpoint = self.__ENDPOINT + '/info'
        return self.requester.request(endpoint, params)

    # /map endpoint
    def map(self, listing_status=None, start=None, limit=None, symbol=None):
        params = self.construct_params('listing_status', listing_status) if listing_status != None else ''
        params += '&' + self.construct_params('start', start) if start != None else ''
        params += '&' + self.construct_params('limit', limit) if limit != None else ''
        params += '&' + self.construct_params('symbol', symbol) if symbol != None else ''

        endpoint = self.__ENDPOINT + '/map'
        return self.requester.request(endpoint, params)

    def market_pairs(self):
        # TODO
        return

    def ohlcv(self):
        # TODO
        return

    def quotes(self):
        # TODO
        return

class Exchange:
    __ENDPOINT = '/v1/exchange'

    def info(self):
        # TODO
        return

    def map(self):
        # TODO
        return

    def listings(self):
        # TODO
        return

    def market_pairs(self):
        # TODO
        return

    def quotes(self):
        # TODO
        return

class GlobalMetrics:
    __ENDPOINT = '/v1/global-metrics'

    def quotes(self):
        # TODO
        return

class Tools:
    __ENDPOINT = '/v1/tools'

    def price_convertion(self):
        # TODO
        return

class Listings(EndpointType):

    def __init__(self, requester, base_endpoint):
        EndpointType.__init__(self, requester)
        self.endpoint = base_endpoint + '/listings'

    def construct_multiple_params(self, start=None, limit=None, convert=None, sort=None,
        sort_dir=None, cryptocurrency_type=None):
        params = self.construct_params('start', start) if start != None else ''
        params += '&' + self.construct_params('limit', limit) if limit != None else ''
        params += '&' + self.construct_params('convert', convert) if convert != None else ''
        params += '&' + self.construct_params('sort', sort) if sort != None else ''
        params += '&' + self.construct_params('sort_dir', sort_dir) if sort_dir != None else ''
        params += '&' + self.construct_params('cryptocurrency_type', cryptocurrency_type) if cryptocurrency_type != None else ''
        return params

    # get latest listings
    def latest(self, start=None, limit=None, convert=None, sort=None,
        sort_dir=None, cryptocurrency_type=None):
        params = self.construct_multiple_params(start=start, limit=limit, convert=convert,
            sort=sort, sort_dir=sort_dir, cryptocurrency_type=cryptocurrency_type)
        endpoint = self.endpoint + '/latest'
        return self.requester.request(endpoint, params)

    # get historical listings
    def historical(self, timestamp=None, start=None, limit=None, convert=None,
        sort=None, sort_dir=None, cryptocurrency_type=None):
        params = self.construct_multiple_params(start=start, limit=limit, convert=convert,
            sort=sort, sort_dir=sort_dir, cryptocurrency_type=cryptocurrency_type)
        endpoint = self.endpoint + '/historical'
        return self.requester.request(endpoint, params)