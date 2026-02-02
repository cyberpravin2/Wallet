from bot.database import wallet_logs_col
from datetime import datetime


def add_wallet_log(user_id: int, log_type: str, amount: int, note: str = ""):
    wallet_logs_col.insert_one({
        "user_id": user_id,
        "type": log_type,  # deposit, withdraw, task_earning, transfer
        "amount": amount,
        "note": note,
        "created_at": datetime.utcnow()
    })
