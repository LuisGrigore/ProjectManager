from typing import Dict

from flask import request
from returns.result import Result

from project_manager.controllers.manage_network_results import manage_network_result
from project_manager.dtos.fragment_dtos import FragmentCreateDto, FragmentGetDto
from project_manager.errors.network_base_error import NetworkError
from project_manager.repos import project_repos
from project_manager.services import fragment_service


def register(app):
    @app.route('/fragments', methods=['POST'])
    def create_fragment():
        fragment_create_data: Dict = request.get_json()
        fragment_create: FragmentCreateDto = FragmentCreateDto()
        fragment_create.deserialize(fragment_create_data)
        fragment_created: Result[FragmentGetDto, NetworkError] = fragment_service.create_fragment(fragment_create,
                                                                                              project_repos.get_project)
        return manage_network_result(fragment_created)

    @app.route('/fragments/<id>', methods=['GET'])
    def get_fragment_by_id(id: str):
        get_fragment_dto = fragment_service.find_fragment_by_id(id)
        return manage_network_result(get_fragment_dto)