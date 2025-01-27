from typing import Optional, Any, Type, List

from flask_sqlalchemy.model import Model
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from project_manager.app import db


def save_entity(entity: Model) -> Optional[Model]:
    if _add_to_session(db.session, entity) and _commit_changes(db.session):
        return entity
    return None

def get_entity_by_id(entity_id: Any, model: Type[Model]) -> Optional[Model]:
    return _get_entity(db.session, model, entity_id)

def update_entity(entity_id: Any, updated_entity: Model, model: Type[Model]) -> Optional[Model]:
    entity = _get_entity(db.session, model, entity_id)
    if entity:
        for attr, value in vars(updated_entity).items():
            if not attr.startswith("_"):
                setattr(entity, attr, value)
        if _commit_changes(db.session):
            return entity
    return None

def delete_entity_by_id(entity_id: int, model: Type[Model]) -> Optional[Model]:
    entity = _get_entity(db.session, model, entity_id)
    if entity and _delete_from_session(db.session, entity) and _commit_changes(db.session):
        return entity
    return None



def _commit_changes(session: Session) -> bool:
    try:
        session.commit()
        return True
    except SQLAlchemyError:
        session.rollback()
        return False

def _add_to_session(session: Session, entity: Model) -> bool:
    try:
        session.add(entity)
        return True
    except SQLAlchemyError:
        return False

def _delete_from_session(session: Session, entity: Model) -> bool:
    try:
        session.delete(entity)
        return True
    except SQLAlchemyError:
        return False

def _get_entity(session: Session, model: Type[Model], entity_id: Any) -> Optional[Model]:
    return session.get(model, entity_id)