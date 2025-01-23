from typing import Callable, Optional


from project_manager.dtos.user_dtos import UserLoginDto, UserGetDto
from project_manager.model import UserModel


def validate_login(user_login_dto: UserLoginDto, find_in_db_funct: Callable[[str,str],Optional[UserModel]]) -> bool:
    '''hola'''
    user = find_in_db_funct(user_login_dto.name,user_login_dto.password)
    if user:
        return True
    return False
