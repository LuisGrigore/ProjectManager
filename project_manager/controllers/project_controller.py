from typing import Dict
from flask import request
from returns.result import Result, Success

from project_manager.controllers.manage_network_results import manage_network_result
from project_manager.dtos.project_dtos import ProjectCreateDto, ProjectCreatedDto
from project_manager.errors.network_base_error import NetworkError
from project_manager.repos.project_repos import save_project
from project_manager.services import project_service


def register(app):
    @app.route('/projects', methods = ['POST'])
    def create_project():
        project_create_data: Dict = request.get_json()
        project_create: ProjectCreateDto = ProjectCreateDto()
        project_create.deserialize(project_create_data)
        project_created: Result[ProjectCreatedDto, NetworkError] = project_service.create_project(project_create,save_project)

        return manage_network_result(project_created)


    @app.route('/<uid>/projects')
    def get_projects_by_owner_id():
        pass

    @app.route('/projects/<id>')
    def get_project_by_id():
        pass

    @app.route('/askjdfbgh')
    def assign_project_to():
        pass

    @app.route('/lhsdkfj')
    def delete_project():
        pass