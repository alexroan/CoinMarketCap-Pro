# CoinMarketCap Pro API Wrapper

Use this library to easily retrieve data from [Coinmarketcap.com professional API](https://pro.coinmarketcap.com/)

You can also use the [Sandbox API](https://sandbox.coinmarketcap.com) to develop with

## Basic Usage

```python

from coin_market_cap import CoinMarketCap, ApiUrl

# Use the SANDBOX_URL for the sandbox, or BASE_URL for the pro API
# Use your api key
coinmarketcap = CoinMarketCap(
    url=ApiUrl.SANDBOX_URL, 
    api_key='example-api-key')

# Accesssing the /cryptocurrency/info endpoint
results = coinmarketcap.cryptocurrency.info(symbol='TRX')

```

## Endpoints supported

For full list of endpoints in the new professional API visit the [Official API Documentation](https://pro.coinmarketcap.com/api/v1)

```python
# Cryptocurrency endpoints
coinmarketcap.cryptocurrency.info(...)
coinmarketcap.cryptocurrency.map(...)
coinmarketcap.cryptocurrency.listings.latest(...)
coinmarketcap.cryptocurrency.listings.latest(...)
coinmarketcap.cryptocurrency.market_pairs.latest(...)
coinmarketcap.cryptocurrency.ohlcv.historical(...)
coinmarketcap.cryptocurrency.ohlcv.latest(...)
coinmarketcap.cryptocurrency.quotes.historical(...)
coinmarketcap.cryptocurrency.quotes.latest(...)

# Exchange endpoints
coinmarketcap.exchange.info(...)
coinmarketcap.exchange.map(...)
coinmarketcap.exchange.listings.historical(...)
coinmarketcap.exchange.listings.latest(...)
coinmarketcap.exchange.market_pairs.latest(...)
coinmarketcap.exchange.quotes.historical(...)
coinmarketcap.exchange.quotes.latest(...)

# Global metrics endpoints
coinmarketcap.global_metrics.quotes.historical(...)
coinmarketcap.global_metrics.quotes.latest(...)

# Tools endpoints
coinmarketcap.tools.price_conversion(...)
```
