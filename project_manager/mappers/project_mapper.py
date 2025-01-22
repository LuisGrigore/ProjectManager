from project_manager.dtos.project_dtos import ProjectCreatedDto, ProjectCreateDto
from project_manager.model.model import ProjectModel


def project_create_dto_to_project_model(project_create: ProjectCreateDto) -> ProjectModel:
    user_model: ProjectModel = ProjectModel.get_ProjectModel(project_create.name, project_create.owner_id)
    return user_model

def project_model_to_project_created_dto(project_model: ProjectModel) -> ProjectCreatedDto:
    user_create_dto: ProjectCreatedDto = ProjectCreatedDto(project_model.name, project_model.owner_id)
    return user_create_dto