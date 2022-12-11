from dotenv import load_dotenv
import os

load_dotenv()


import os

class Config:
    # Set the MongoDB URI for the development environment
    MONGO_URI_DEV = os.getenv("MONGO_URI_DEV")

    # Set the MongoDB URI for the production environment
    MONGO_URI_PROD = os.getenv("MONGO_URI_PROD")

    # Set the MongoDB URI for the test environment
    MONGO_URI_TEST = os.getenv("MONGO_URI_TEST")
    


    
