from pymongo import MongoClient
from bot.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Core collections
users_col = db.users
wallet_logs_col = db.wallet_logs

# Money flow
deposits_col = db.deposits
withdraws_col = db.withdraws

# Task system
tasks_col = db.tasks
task_submissions_col = db.task_submissions

# Disputes & settings
disputes_col = db.disputes
settings_col = db.settings
