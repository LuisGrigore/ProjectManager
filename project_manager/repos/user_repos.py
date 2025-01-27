from typing import Optional

from project_manager.model import UserModel
from project_manager.repos.base_functs import save_entity, get_entity_by_id, update_entity, delete_entity_by_id


def save_user(user: UserModel) -> Optional[UserModel]:
    return save_entity(user)

def get_user(uid: int) -> Optional[UserModel]:
    return get_entity_by_id(uid,UserModel)


def update_user(uid: int, updated_user: UserModel) -> Optional[UserModel]:
    return update_entity(uid,updated_user,UserModel)


def delete_user_by_id(uid: int) -> Optional[UserModel]:
    return delete_entity_by_id(uid)


def get_user_by_name_password(name: str, password: str) -> Optional[UserModel]:
    user = UserModel.query.filter(UserModel.name == name, UserModel.password == password).first()
    if user:
        return user
    return None

