from keys import key1, key2

# import packages
# install alpaca if you need to
import alpaca_trade_api as tradeapi
import sqlite3 as sql
import os
import pandas as pd
from datetime import datetime

# define api variable to work with Alpaca
os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"

# insert your api keys here
api = tradeapi.REST(key1, key2, api_version='v2')

assets = api.list_assets(status='active')
# remove some undesired assets because SQL table names cannot include periods
assets = [a.symbol for a in assets if a.symbol[-2:] != '.U']
assets = [a for a in assets if a[-2:] != '.A']
assets = [a for a in assets if a[-2:] != '.B']
assets = [a for a in assets if a[-2:] != '.C']
assets = [a for a in assets if a[-3:] != '.RT']
# these key words also do not work as table names
assets.remove('OR')
assets.remove('ELSE')
assets.remove('ALL')

# filter list down to the first 1000
assets = assets[0:1000]

# establish database connection
conn = sql.connect('stockData.db') 

# loop through the assets list, collect data for each, and create a table in the db
for ticker in assets:
    data = api.get_barset(ticker, 'day',1000)[ticker].df
    # use PANDAS to send your df to a table in the db
    data.to_sql(f"{ticker}", conn)   
    
conn.commit()
conn.close()