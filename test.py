from market import Market

coinmarketcap = Market(api_key='key')
print(coinmarketcap.cryptocurrency.info(id='example-id'))