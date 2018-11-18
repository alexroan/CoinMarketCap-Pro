class EndpointType:

    def __init__(self, requester):
        self.requester = requester

    # construct many parameters
    def construct_multiple_params(self, **kwargs):
        params = ''
        for key in kwargs:
            params += '&' + self.construct_param(key, kwargs[key]) if kwargs[key] != None else ''
        return params

    def construct_param(self, key, value):
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

    def check_id_or_symbol(self, id, symbol):
        if id == None and symbol == None:
            raise Exception('Needs at least one of id or symbol')
        if id != None and symbol != None:
            raise Exception('Either id or symbol, not both')


class Cryptocurrency(EndpointType):
    __ENDPOINT = '/v1/cryptocurrency'

    def __init__(self, requester):
        EndpointType.__init__(self, requester=requester)
        self.listings = Listings(requester=self.requester, base_endpoint=self.__ENDPOINT)
        self.market_pairs = MarketPairs(requester=self.requester, base_endpoint=self.__ENDPOINT)
        self.ohlcv = OHLCV(requester=self.requester, base_endpoint=self.__ENDPOINT)
        self.quotes = Quotes(requester=self.requester, base_endpoint=self.__ENDPOINT)

    # info endpoint.
    def info(self, id=None, symbol=None):
        self.check_id_or_symbol(id, symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol)
        endpoint = self.__ENDPOINT + '/info'
        return self.requester.request(endpoint, params)

    # map endpoint
    def map(self, listing_status=None, start=None, limit=None, symbol=None):
        params = self.construct_multiple_params(listing_status=listing_status, start=start, limit=limit, symbol=symbol)
        endpoint = self.__ENDPOINT + '/map'
        return self.requester.request(endpoint, params)


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

class Quotes(EndpointType):

    def __init__(self, requester, base_endpoint):
        EndpointType.__init__(self, requester)
        self.endpoint = base_endpoint + '/quotes'

    # get historical quotes
    def historical(self, id=None, symbol=None, time_start=None, time_end=None, count=None,
        interval=None, convert=None):
        self.check_id_or_symbol(id=id, symbol=symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol, time_start=time_start,
            time_end=time_end, count=count, interval=interval, convert=convert)
        endpoint = self.endpoint + '/historical'
        return self.requester.request(endpoint, params)

    # get latest quotes
    def latest(self, id=None, symbol=None, convert=None):
        self.check_id_or_symbol(id=id, symbol=symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol, convert=convert)
        endpoint = self.endpoint + '/latest'
        return self.requester.request(endpoint, params)


class OHLCV(EndpointType):

    def __init__(self, requester, base_endpoint):
        EndpointType.__init__(self, requester)
        self.endpoint = base_endpoint + '/ohlcv'

    # get historical ohlcv
    def historical(self, id=None, symbol=None, time_period=None, time_start=None,
        time_end=None, count=None, interval=None, convert=None):
        self.check_id_or_symbol(id=id, symbol=symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol, time_period=time_period,
            time_start=time_start, time_end=time_end, count=count, interval=interval, convert=convert)
        endpoint = self.endpoint + '/historical'
        return self.requester.request(endpoint, params)

    # get latest ohlcv
    def latest(self, id=None, symbol=None, convert=None):
        self.check_id_or_symbol(id=id, symbol=symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol, convert=convert)
        endpoint = self.endpoint + '/latest'
        return self.requester.request(endpoint, params)


class MarketPairs(EndpointType):

    def __init__(self, requester, base_endpoint):
        EndpointType.__init__(self, requester)
        self.endpoint = base_endpoint + '/market-pairs'

    # get latest market pairs
    def latest(self, id=None, symbol=None, start=None, limit=None, convert=None):
        self.check_id_or_symbol(id=id, symbol=symbol)
        params = self.construct_multiple_params(id=id, symbol=symbol, start=start, limit=limit, convert=convert)
        endpoint = self.endpoint + '/latest'
        return self.requester.request(endpoint, params)


class Listings(EndpointType):

    def __init__(self, requester, base_endpoint):
        EndpointType.__init__(self, requester)
        self.endpoint = base_endpoint + '/listings'

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