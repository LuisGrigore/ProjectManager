from typing import Optional

from project_manager.app import db
from project_manager.model.model import ProjectModel


def save_project(project: ProjectModel) -> Optional[ProjectModel]:
    try:
        db.session.add(project)
        db.session.commit()
        return project
    except Exception as e:
        print(e)
        return None