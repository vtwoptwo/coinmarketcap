from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

#select environment variables and configure db

if os.getenv('ENV') == 'dev':
    print('Running in development Mode') 
    app.config["MONGO_URI"] = Config.MONGO_URI_DEV
elif os.getenv('ENV') == 'prod':
    print('Running in production Mode')
    app.config["MONGO_URI"] = Config.MONGO_URI_PROD

elif os.getenv('ENV') == 'test':
    print('Running in test Mode')
    app.config["MONGO_URI"] = Config.MONGO_URI_TEST
else:
    print("No environment variable set. Please set ENV to 'dev' or 'prod'")
    exit()

mongo = PyMongo(app)


from backend_api import routes

with app.app_context():

   
