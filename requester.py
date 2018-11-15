import requests

class Requester:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'X-CMC_PRO_API_KEY': api_key
        })

    def request(self, endpoint, params):
        response = self.session.get(
            url=self.base_url + endpoint,
            params=params
        )
        return self.parse_response(response)

    @staticmethod
    def parse_response(response):
        response_dict = response.json()
        if response.status_code == 200:
            return response_dict['data']
        else:
            error_message = response_dict['status']['error_message']
            raise Exception(
                str(response.status_code) + ': ' + error_message)