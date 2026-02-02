from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["monkey_wallet_bot"]

users_col = db.users
wallet_logs_col = db.wallet_logs
