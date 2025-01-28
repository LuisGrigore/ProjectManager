from typing import Optional

from project_manager.model import UserModel
from project_manager.repos import repos


def save_user(user: UserModel) -> Optional[UserModel]:
    return repos.save_entity(user)

def get_user(uid: int) -> Optional[UserModel]:
    return repos.get_entity_by_id(uid,UserModel)


def update_user(uid: int, updated_user: UserModel) -> Optional[UserModel]:
    return repos.update_entity(uid,updated_user,UserModel)


def delete_user_by_id(uid: int) -> Optional[UserModel]:
    return repos.delete_entity_by_id(uid, UserModel)


def get_user_by_name_password(name: str, password: str) -> Optional[UserModel]:
    return repos.get_entity_by_attributes(UserModel, {'name':name, 'password':password})

