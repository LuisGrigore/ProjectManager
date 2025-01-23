from typing import Callable, Optional
from returns.result import Result, Success, Failure

from project_manager.dtos import UserCreateDto, UserCreatedDto, UserGetDto
from project_manager.errors.my_errors import UserNotPersistedError, UserNotFoundError
from project_manager.mappers.user_mapper import user_create_dto_to_user_model, user_model_to_user_created_dto
from project_manager.model import UserModel


def create_user(user_dto:UserCreateDto, persist_funct: Callable[[UserModel], Optional[UserModel]]) -> Result[UserCreatedDto, UserNotPersistedError]:
    '''hola'''
    user_model: UserModel = user_create_dto_to_user_model(user_dto)
    user_model_persisted = persist_funct(user_model)
    if user_model_persisted:
        user_created_dto: UserCreatedDto = user_model_to_user_created_dto(user_model)
        return Success(user_created_dto)
    return Failure(UserNotPersistedError())


def find_user_by_id(uid: int, find_in_db_funct: Callable[[int],Optional[UserModel]]) -> Result[UserGetDto, UserNotFoundError]:
    '''hola'''
    user = find_in_db_funct(uid)
    if user:
        return Success(UserGetDto(user.name))
    return Failure(UserNotFoundError())

