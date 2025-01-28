from returns.result import Result

from project_manager.dtos import UserCreateDto, UserGetDto
from project_manager.errors.my_errors import UserNotPersistedError, UserNotFoundError
from project_manager.mappers import user_mapper
from project_manager.repos import user_repos
from project_manager.services.service import save_entity, find_by_id


def create_user(user_dto:UserCreateDto) -> Result[UserGetDto, UserNotPersistedError]:
    '''hola'''
    return save_entity(user_dto, UserNotPersistedError(), user_repos.save_user,
                       user_mapper.user_create_dto_to_user_model,
                       user_mapper.user_model_to_user_get_dto)

def find_user_by_id(uid: int) -> Result[UserGetDto, UserNotFoundError]:
    '''hola'''
    return find_by_id(uid,user_repos.get_user,UserNotFoundError(),user_mapper.user_model_to_user_get_dto)

