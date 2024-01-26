import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('DB_HOST')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')

uri = f'mongodb+srv://{USER}:{PASSWORD}@{HOST}/?retryWrites=true&w=majority'

print(uri)

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))