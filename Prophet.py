import ccxt
import pandas as pd
import json
from pandas.io.json import json_normalize

hitbtc = ccxt.hitbtc({'verbose': True})
bitmex = ccxt.bitmex()
poloniex = ccxt.poloniex()
exmo   = ccxt.exmo({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})
kraken = ccxt.kraken({
    'apiKey': 'YOUR_PUBLIC_API_KEY',
    'secret': 'YOUR_SECRET_PRIVATE_KEY',
})

exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})

hitbtc_markets = hitbtc.load_markets()

print(hitbtc.id, hitbtc_markets)
print(bitmex.id, bitmex.load_markets())

#fetch and write trades bitcoin BTC/USD
print(bitmex.fetch_trades('BTC/USD'))
df_btc = pd.DataFrame(bitmex.fetch_trades('BTC/USD'))
df_btc.to_csv("c:/prophet/bitmex_BTC_response.csv", sep=',', encoding='utf-8')

#fetch and write trades Ethertium ETH/USD
print(bitmex.fetch_trades('ETH/USD'))
df_eth = pd.DataFrame(bitmex.fetch_trades('ETH/USD'))
df_eth.to_csv("c:/prophet/bitmex_ETH_response.csv", sep=',', encoding='utf-8')

#fetch and write trades Ethertium ETH/USD
#
df_eth = pd.DataFrame(poloniex.fetch_trades('ETH/USDT',since=1514808826000))
df_eth.to_csv("c:/prophet/poliniex ETH_response.csv", sep=',', encoding='utf-8')





print(huobi.id, huobi.load_markets())

print(hitbtc.fetch_order_book(hitbtc.symbols[0]))
print(bitmex.fetch_ticker('BTC/USD'))
print(huobi.fetch_trades('LTC/CNY'))

print(exmo.fetch_balance())

# sell one ฿ for market price and receive $ right now
print(exmo.id, exmo.create_market_sell_order('BTC/USD', 1))

# limit buy BTC/EUR, you pay €2500 and receive ฿1  when the order is closed
print(exmo.id, exmo.create_limit_buy_order('BTC/EUR', 1, 2500.00))

# pass/redefine custom exchange-specific order params: type, amount, price, flags, etc...
kraken.create_market_buy_order('BTC/USD', 1, {'trading_agreement': 'agree'})
