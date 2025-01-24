from project_manager.dtos import UserCreateDto, UserGetDto
from project_manager.model import UserModel


def user_create_dto_to_user_model(user_create: UserCreateDto) -> UserModel:
    user_model: UserModel = UserModel.get_UserModel(user_create.name, user_create.password)
    return user_model

def user_model_to_user_get_dto(user_model: UserModel) -> UserGetDto:
    user_get_dto: UserGetDto = UserGetDto(user_model.name, user_model.id)
    return user_get_dto