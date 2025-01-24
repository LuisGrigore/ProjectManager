from typing import Optional, List

from project_manager.app import db
from project_manager.model.model import ProjectModel


def save_project(project: ProjectModel) -> Optional[ProjectModel]:
    try:
        db.session.add(project)
        db.session.commit()
        return project
    except Exception as e:
        return None

def find_projects_by_user_id(uid: int) -> Optional[List[ProjectModel]]:
    try:
        projects: List[ProjectModel] = ProjectModel.query.filter(ProjectModel.owner_id == uid).all()
        if len(projects) == 0:
            return None
        return projects
    except Exception as e:
        return None