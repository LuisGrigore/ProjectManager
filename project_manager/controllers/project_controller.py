from typing import Dict, List
from flask import request
from returns.result import Result

from project_manager.controllers.manage_network_results import manage_network_result, manage_network_result_with_list
from project_manager.dtos.project_dtos import ProjectCreateDto, ProjectGetDto
from project_manager.errors.network_base_error import NetworkError
from project_manager.repos import project_repos, user_repos
from project_manager.services import project_service


def register(app):
    @app.route('/projects', methods = ['POST'])
    def create_project():
        project_create_data: Dict = request.get_json()
        project_create: ProjectCreateDto = ProjectCreateDto()
        project_create.deserialize(project_create_data)
        project_created: Result[ProjectGetDto, NetworkError] = project_service.create_project(project_create, project_repos.save_project, user_repos.get_user)

        return manage_network_result(project_created)

    @app.route('/users/<uid>/projects', methods = ['GET'])
    def get_projects_by_owner_id(uid: int):
        projects: Result[List[ProjectGetDto], NetworkError] = project_service.get_projects_by_owner_id(uid, project_repos.find_projects_by_user_id)
        return manage_network_result_with_list(projects)

    @app.route('/projects/<id>', methods = ['GET'])
    def get_project_by_id(id: str):
        get_project_dto = project_service.find_project_by_id(id, project_repos.get_project)
        return manage_network_result(get_project_dto)

    @app.route('/projects/add-member', methods = ['POST'])
    def assign_project_to():
        pass

    @app.route('/projects/delete/<id>', methods = ['DELETE'])
    def delete_project(id: str):
        pass