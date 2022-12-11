from flask import Flask, render_template, request, jsonify
from backend_api import mongo, app
from api_call import call


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html', form=request.form)

    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/coins', methods=['GET'])
def get_coins():
    print("Collecting coins...")
    collection = mongo.db.coins
    coins = collection.find()
    output = []
    for coin in coins:
        output.append({'symbol': coin['symbol'], 'price': coin['price'], 'market_cap': coin['market_cap'], 'market_cap_pct': coin['market_cap_pct'], 'last_updated': coin['last_updated']})
    
    output.sort(key=lambda x: x['last_updated'], reverse=True)
    return render_template('coins.html', coins=output)

@app.route('/api_call', methods=['GET'])
def api_call(): 
    call()
    print("Calling API...")
    return 200