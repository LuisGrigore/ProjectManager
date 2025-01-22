from typing import Callable, Optional

from project_manager.dtos.project_dtos import ProjectCreateDto, ProjectCreatedDto
from project_manager.errors.my_errors import ProjectNotPersistedError
from project_manager.mappers.project_mapper import project_create_dto_to_project_model, \
    project_model_to_project_created_dto
from project_manager.model.model import ProjectModel
from returns.result import Result, Success, Failure


def create_project(project_dto:ProjectCreateDto, persist_funct: Callable[[ProjectModel], Optional[ProjectModel]]) -> Result[ProjectCreatedDto, ProjectNotPersistedError]:
    '''hola'''
    project_model: ProjectModel = project_create_dto_to_project_model(project_dto)
    project_model_persisted = persist_funct(project_model)
    if project_model_persisted:
        project_created_dto: ProjectCreatedDto = project_model_to_project_created_dto(project_model)
        return Success(project_created_dto)
    return Failure(ProjectNotPersistedError())