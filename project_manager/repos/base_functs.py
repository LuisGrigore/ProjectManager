from typing import Optional, Any, Type

from flask_sqlalchemy.model import Model

from project_manager.app import db
from project_manager.model import UserModel


def save_entity(entity: Model) -> Optional[Model]:
    try:
        db.session.add(entity)
        db.session.commit()
        return entity
    except:
        return None

def get_entity_by_id(id:Any, model: Type[Model]) -> Optional[Model]:
    entity = model.query.get(id)
    if entity:
        return entity
    return None

def update_entity(id: Any, updated_entity: Model, model: Type[Model]) -> Optional[Model]:
    entity = db.session.get(id)
    if entity:
        model.update(entity, updated_entity)
        db.session.commit()
        return entity
    return None

def delete_entity_by_id(id: int) -> Optional[Model]:
    entity = db.session.get(id)
    if entity:
        try:
            db.session.delete(entity)
            db.session.commit()
            return entity
        except:
            return None
    return None