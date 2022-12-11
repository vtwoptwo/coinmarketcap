from dotenv import load_dotenv
import os
import requests
from flask_pymongo import PyMongo
from backend_api import app, mongo

collection = mongo.db.coins
load_dotenv()

BASE = os.getenv('CMC_BASE')
ENDPOINT = os.getenv('CMC_EP')
KEY = os.getenv('API_KEY')


params = {
    "sort": "market_cap",
    "sort_dir": "desc",
    "limit": 10
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": KEY
}

response = requests.get(BASE+ENDPOINT, params=params, headers=headers)
print(response)
data = response.json()

total_market_cap = 0

for coin in data["data"]:
    total_market_cap += coin["quote"]["USD"]["market_cap"]

for coin in data["data"]:
    symbol = coin["symbol"]
    price = coin["quote"]["USD"]["price"]
    market_cap = coin["quote"]["USD"]["market_cap"]
    market_cap_pct = market_cap / total_market_cap
    last_updated = coin["last_updated"]


    document = {
        "symbol": symbol,
        "price": price,
        "market_cap": market_cap,
        "market_cap_pct": market_cap_pct,
        "last_updated": last_updated
    }

    
    collection.insert_one(document)


