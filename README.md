Example usage:

```

from coin_market_cap import CoinMarketCap, ApiUrl

coinmarketcap = CoinMarketCap(
    url=ApiUrl.SANDBOX_URL, 
    api_key='example-api-key')

results = coinmarketcap.cryptocurrency.info(symbol='TRX')

```