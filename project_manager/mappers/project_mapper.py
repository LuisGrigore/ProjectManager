from project_manager.dtos.project_dtos import ProjectGetDto, ProjectCreateDto
from project_manager.model.model import ProjectModel


def project_create_dto_to_project_model(project_create: ProjectCreateDto) -> ProjectModel:
    project_model: ProjectModel = ProjectModel.get_ProjectModel(project_create.name, project_create.owner_id)
    return project_model

def project_model_to_project_get_dto(project_model: ProjectModel) -> ProjectGetDto:
    project_get_dto: ProjectGetDto = ProjectGetDto(project_model.name, project_model.owner_id)
    return project_get_dto