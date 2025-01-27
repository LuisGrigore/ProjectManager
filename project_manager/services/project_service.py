from typing import Callable, List

from project_manager.dtos.project_dtos import ProjectCreateDto, ProjectGetDto
from project_manager.errors.my_errors import ProjectNotPersistedError, UserNotFoundError, ProjectNotFoundError
from project_manager.mappers import project_mapper
from project_manager.mappers.project_mapper import project_model_to_project_get_dto
from project_manager.model.model import ProjectModel
from returns.result import Result, Success, Failure

from project_manager.repos import project_repos
from project_manager.services.base_functs import save_entity, find_by_id


def create_project(project_dto:ProjectCreateDto, user_exists_funct: Callable[[int],bool]) -> Result[ProjectGetDto, ProjectNotPersistedError]:
    '''hola'''
    if user_exists_funct(project_dto.owner_id):
        return save_entity(project_dto,ProjectNotPersistedError(),project_repos.save_project,project_mapper.project_create_dto_to_project_model,project_mapper.project_model_to_project_get_dto)
    return Failure(UserNotFoundError())


def get_projects_by_owner_id(uid: int, get_projects_by_user_id_funct: Callable[[int], List[ProjectModel]]) -> Result[List[ProjectGetDto], ProjectNotFoundError]:
    found_projects: List[ProjectModel] = get_projects_by_user_id_funct(uid)
    if found_projects:
        project_gets: List[ProjectGetDto] = [project_model_to_project_get_dto(x) for x in found_projects]
        return Success(project_gets)
    return Failure(ProjectNotFoundError())


def find_project_by_id(id, get_project_funct):
    '''hola'''
    return find_by_id(id,get_project_funct,ProjectNotFoundError(),project_mapper.project_model_to_project_get_dto)