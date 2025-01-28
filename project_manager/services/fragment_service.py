from typing import Callable

from returns.result import Failure, Result

from project_manager.dtos.fragment_dtos import FragmentCreateDto, FragmentGetDto
from project_manager.errors.my_errors import ProjectNotFoundError, FragmentNotPersistedError, FragmentNotFoundError
from project_manager.mappers import fragment_mapper
from project_manager.repos import fragment_repos
from project_manager.services import service


def create_fragment(fragment_dto:FragmentCreateDto, project_exists_funct: Callable[[int],bool]) -> Result[FragmentGetDto, FragmentNotPersistedError]:
    '''hola'''
    if project_exists_funct(fragment_dto.project_id):
        return service.save_entity(fragment_dto, FragmentNotPersistedError(), fragment_repos.save_fragment, fragment_mapper.fragment_create_dto_to_fragment_model, fragment_mapper.fragment_model_to_fragment_get_dto)
    return Failure(ProjectNotFoundError())



def find_fragment_by_id(id):
    '''hola'''
    return service.find_by_id(id, fragment_repos.get_fragment, FragmentNotFoundError(), fragment_mapper.fragment_model_to_fragment_get_dto)