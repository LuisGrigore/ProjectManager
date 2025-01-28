from typing import Optional, Any, Type, Callable, Dict

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
    return (
        entity if entity and all(
            setattr(entity, attr, value) for attr, value in vars(updated_entity).items() if not attr.startswith("_")
        ) and _commit_changes(db.session)
        else None
    )

def delete_entity_by_id(entity_id: int, model: Type[Model]) -> Optional[Model]:
    entity = _get_entity(db.session, model, entity_id)
    if entity and _delete_from_session(db.session, entity) and _commit_changes(db.session):
        return entity
    return None

def get_entity_by_attributes(model:Type[Model], filters: Dict[str,Any]):
    query = model.query
    if filters:
        for field, value in filters.items():
            query = query.filter(getattr(model, field) == value)
    return query.all()


def _commit_changes(session: Session) -> bool:
    return _try_true_except_false(session.commit)


def _add_to_session(session: Session, entity: Model) -> bool:
    return _try_true_except_false(lambda : session.add(entity))


def _delete_from_session(session: Session, entity: Model) -> bool:
    return _try_true_except_false(lambda: session.delete(entity))


def _get_entity(session: Session, model: Type[Model], entity_id: Any) -> Optional[Model]:
    return session.get(model, entity_id)

def _try_true_except_false(*ops: Callable) -> bool:
    try:
        for op in ops:
            op()
        return True
    except SQLAlchemyError:
        return False