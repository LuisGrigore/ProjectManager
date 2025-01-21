from typing import Callable, Optional
from returns.result import Result, Success, Failure

from project_manager.dtos import UserCreateDto, UserCreatedDto, UserGetDto
from project_manager.errors.my_errors import UserNotPersistedError
from project_manager.mappers.user_mapper import user_create_dto_to_user_model, user_model_to_user_created_dto
from project_manager.model import UserModel


def create_user(user_dto:UserCreateDto, persist_funct: Callable[[UserModel], Optional[UserModel]]) -> Result[UserCreatedDto, UserNotPersistedError]:
    user_model: UserModel = user_create_dto_to_user_model(user_dto)
    user_created: UserCreatedDto = user_model_to_user_created_dto(user_model)
    if persist_funct:
        if not persist_funct(user_model):
            return Failure(UserNotPersistedError())
    return Success(user_created)

def find_user_by_id(uid: int, find_in_db_funct: Callable[[int],Optional[UserModel]]) -> Optional[UserGetDto]:
    user = find_in_db_funct(uid)
    if user:
        return UserGetDto(user.name)
    return None