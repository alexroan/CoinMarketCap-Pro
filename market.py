from endpoint_type import Cryptocurrency

class Market:

    __BASE_URL = 'https://pro-api.coinmarketcap.com'
    __SANDBOX_URL = 'https://sandbox-api.coinmarketcap.com'

    def __init__(self, api_key):
        self.api_key = api_key
        self.cryptocurrency = Cryptocurrency(url=self.__BASE_URL, api_key=self.api_key)