from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
import json


load_dotenv()


app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/coinmarketcap'
mongo = PyMongo(app)

import requests

URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'
KEY = os.getenv('API_KEY')


params = {
    "data": '2018-09-15',
    "sort": "market_cap",
    "sort_dir": "desc",
    "limit": 10
}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": '8db8debd-b885-4495-8977-0c135a251086'
}

response = requests.get(URL, params=params, headers=headers)

data = response.json()
print(data)

data = "./data.json"
with open(data) as f:
    data = json.load(f)
print(data)

total_market_cap = 0
#first get the total market cap of the whole call response
for coin in data["data"]:
    total_market_cap += coin["quote"]["USD"]["market_cap"]

for coin in data["data"]:
    symbol = coin["symbol"]
    price = coin["quote"]["USD"]["price"]
    market_cap = coin["quote"]["USD"]["market_cap"]
    market_cap_pct = market_cap / total_market_cap
    last_updated = coin["last_updated"]



    collection = mongo.db.coins

    document = {
        "symbol": symbol,
        "price": price,
        "market_cap": market_cap,
        "market_cap_pct": market_cap_pct,
        "last_updated": last_updated
    }

    collection.insert_one(document)

print(document)


