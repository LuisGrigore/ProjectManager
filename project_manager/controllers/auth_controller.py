from datetime import datetime
from typing import Dict

from auth.auth_session import AuthSession
from flask import request

from auth.config import TTL
from auth.token_model import Token
from project_manager.dtos.user_dtos import UserLoginDto
from project_manager.errors.my_errors import UserNotFoundError
from project_manager.repos.user_repos import get_user_by_name_password
from project_manager.services.auth_service import validate_login
from project_manager.mappers import token_mapper


def register(app, auth_session: AuthSession):
    @app.route('/login', methods = ['POST'])
    def login():
        data: Dict = request.get_json()
        user_login_dto: UserLoginDto = UserLoginDto()
        user_login_dto.deserialize(data)

        if validate_login(user_login_dto, get_user_by_name_password):
            return token_mapper.token_to_token_get_dto(auth_session.add_token(Token(user_login_dto.name,TTL,datetime.now()))).serialize()

        return UserNotFoundError().message, UserNotFoundError().status_code