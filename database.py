from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Users & Wallet
users_col = db.users
wallet_logs_col = db.wallet_logs

# Money flows
deposits_col = db.deposits
withdraws_col = db.withdraws

# Tasks
tasks_col = db.tasks
task_submissions_col = db.task_submissions

# Disputes & Settings
disputes_col = db.disputes
settings_col = db.settings
