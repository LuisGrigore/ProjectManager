from typing import Optional, List

from project_manager.model.model import ProjectModel
from project_manager.repos.repos import save_entity, get_entity_by_id


def save_project(project: ProjectModel) -> Optional[ProjectModel]:
    return save_entity(project)

def find_projects_by_user_id(uid: int) -> Optional[List[ProjectModel]]:
    try:
        projects: List[ProjectModel] = ProjectModel.query.filter(ProjectModel.owner_id == uid).all()
        if len(projects) == 0:
            return None
        return projects
    except Exception as e:
        return None


def get_project(id: str) -> Optional[ProjectModel]:
    return get_entity_by_id(id, ProjectModel)