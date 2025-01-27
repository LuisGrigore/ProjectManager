from typing import Callable, Optional

from returns.result import Success, Failure

from project_manager.dtos.dto_base import CreateDto, GetDto
from project_manager.errors.https_errors import NotPersistedError, NotFoundError
from project_manager.model.model import Model

PersistFunct = Callable[[Model], Optional[Model]]
DtoToModelFunct = Callable[[CreateDto], Model]
ModelToDtoFunct = Callable[[Model], GetDto]

def save_entity(create_dto:CreateDto, error: NotPersistedError, persist_funct: PersistFunct, create_dto_to_model_funct:DtoToModelFunct, model_to_get_dto_funct:ModelToDtoFunct):
    model = create_dto_to_model_funct(create_dto)
    model_persisted = persist_funct(model)
    if model_persisted:
        get_dto = model_to_get_dto_funct(model_persisted)
        return Success(get_dto)
    return Failure(error)

def find_by_id(id:int, persist_funct: PersistFunct, error: NotFoundError, model_to_get_dto_funct:ModelToDtoFunct):
    '''hola'''
    model = persist_funct(id)
    if model:
        return Success(model_to_get_dto_funct(model))
    return Failure(error)