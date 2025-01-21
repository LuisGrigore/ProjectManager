from typing import Dict

from flask import request
from returns.result import Result, Success

from project_manager.dtos import UserCreateDto, UserCreatedDto, UserGetDto
from project_manager.errors.network_base_error import NetworkError, manage_network_result
from project_manager.services import user_service
from project_manager.repos.user_repos import save_user,get_user


def register(app):

    @app.route('/users', methods=['POST'])
    def register_user():
        user_create_data: Dict = request.get_json()
        user_create: UserCreateDto = UserCreateDto()
        user_create.deserialize(user_create_data)

        user_created: Result[UserCreatedDto, NetworkError] = user_service.create_user(user_create,save_user)

        return manage_network_result(user_created)

    @app.route('/users/<uid>', methods=['GET'])
    def get_user_by_id(uid: int):
        get_user_dto = user_service.find_user_by_id(uid, get_user)
        if get_user_dto:
            return UserGetDto.serialize(get_user_dto)
        return "No se pudoi completar la accion"
