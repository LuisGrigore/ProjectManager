from project_manager.dtos import UserCreateDto, UserCreatedDto
from project_manager.model import UserModel


def user_create_dto_to_user_model(user_create: UserCreateDto) -> UserModel:
    user_model: UserModel = UserModel.get_UserModel(user_create.name, user_create.password)
    return user_model

def user_model_to_user_created_dto(user_model: UserModel) -> UserCreatedDto:
    user_create_dto: UserCreatedDto = UserCreatedDto(user_model.name)
    return user_create_dto