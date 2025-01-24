from typing import Callable, Optional, List

from project_manager.dtos.project_dtos import ProjectCreateDto, ProjectGetDto, ProjectGetDto
from project_manager.errors.my_errors import ProjectNotPersistedError, UserNotFoundError, ProjectNotFoundError
from project_manager.mappers.project_mapper import project_create_dto_to_project_model, \
    project_model_to_project_get_dto
from project_manager.model.model import ProjectModel
from returns.result import Result, Success, Failure


def create_project(project_dto:ProjectCreateDto, persist_funct: Callable[[ProjectModel], Optional[ProjectModel]],
                   user_exists_funct: Callable[[int],bool]) -> Result[ProjectGetDto, ProjectNotPersistedError]:
    '''hola'''
    if user_exists_funct(project_dto.owner_id):
        project_model: ProjectModel = project_create_dto_to_project_model(project_dto)
        project_model_persisted = persist_funct(project_model)
        if project_model_persisted:
            project_created_dto: ProjectGetDto = project_model_to_project_get_dto(project_model)
            return Success(project_created_dto)
        return Failure(ProjectNotPersistedError())
    return Failure(UserNotFoundError())


def get_projects_by_owner_id(uid: int, get_projects_by_user_id_funct: Callable[[int], List[ProjectModel]]) -> Result[List[ProjectGetDto], ProjectNotFoundError]:
    found_projects: List[ProjectModel] = get_projects_by_user_id_funct(uid)
    if found_projects:
        project_gets: List[ProjectGetDto] = [project_model_to_project_get_dto(x) for x in found_projects]
        return Success(project_gets)
    return Failure(ProjectNotFoundError())

