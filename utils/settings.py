from bot.database import settings_col

DEFAULT_SETTINGS = {
    "task_upload_fee": 1,        # ₹
    "withdraw_fee_percent": 1    # %
}

def get_settings():
    s = settings_col.find_one({"_id": "global"})
    if not s:
        settings_col.insert_one({"_id": "global", **DEFAULT_SETTINGS})
        return DEFAULT_SETTINGS
    return s

def get_task_upload_fee() -> int:
    return int(get_settings().get("task_upload_fee", 1))

def get_withdraw_fee_percent() -> int:
    return int(get_settings().get("withdraw_fee_percent", 1))

def set_task_upload_fee(amount: int):
    settings_col.update_one(
        {"_id": "global"},
        {"$set": {"task_upload_fee": amount}},
        upsert=True
    )

def set_withdraw_fee_percent(percent: int):
    settings_col.update_one(
        {"_id": "global"},
        {"$set": {"withdraw_fee_percent": percent}},
        upsert=True
)
