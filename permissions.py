from bot.database import users_col

ROLE_USER = "user"
ROLE_TASK_ADMIN = "task_admin"
ROLE_ADMIN = "admin"


def get_user(user_id: int):
    return users_col.find_one({"user_id": user_id})


def get_role(user_id: int) -> str:
    user = get_user(user_id)
    if not user:
        return ROLE_USER
    return user.get("role", ROLE_USER)


def is_admin(user_id: int) -> bool:
    return get_role(user_id) == ROLE_ADMIN


def is_task_admin(user_id: int) -> bool:
    return get_role(user_id) == ROLE_TASK_ADMIN
