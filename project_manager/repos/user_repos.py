from typing import Optional

from project_manager.app import db
from project_manager.model import UserModel

def save_user(user: UserModel) -> Optional[UserModel]:
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as e:
        print(e)
        return None

def get_user(uid: int) -> Optional[UserModel]:
    user = UserModel.query.get(uid)
    if user:
        return user
    return None

def update_user(uid: int, updated_user: UserModel) -> Optional[UserModel]:
    user = db.session.get(uid)
    if user:
        UserModel.update(user, updated_user)
        db.session.commit()
        return user
    return None

def delete_user_by_id(uid: int) -> Optional[UserModel]:
    user = db.session.get(uid)
    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return user
        except:
            return None
    return None

