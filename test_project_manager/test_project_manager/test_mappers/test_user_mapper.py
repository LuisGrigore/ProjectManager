import unittest
from typing import Any

from project_manager.dtos import UserCreateDto
from project_manager.mappers import user_mapper
from project_manager.model import UserModel


class UserMapperTests(unittest.TestCase):

    def test_user_create_dto_to_user_model(self):
        user_create_dto = UserCreateDto(Any)
        user_model = user_mapper.user_create_dto_to_user_model(user_create_dto)
        self.assertIsNotNone(user_model, 'UserModel instance returned by user_mapper.user_create_dto_to_user_model() is None')
        self.assertEqual(user_model.name,user_create_dto.name,'Data not parsed correctly from dto to model')

    def test_user_model_to_user_created_dto(self):
        user_model = UserModel()
        user_model.name = Any
        user_created_dto = user_mapper.user_model_to_user_created_dto(user_model)
        self.assertIsNotNone(user_model,
                             'UserModel instance returned by user_mapper.user_create_dto_to_user_model() is None')
        self.assertEqual(user_model.name, user_created_dto.name,'Data not parsed correctly from dto to model')
