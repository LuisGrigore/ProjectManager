import unittest
from typing import Any

from returns.result import Success, Failure

from project_manager.dtos import UserCreatedDto, UserGetDto
from project_manager.errors.my_errors import UserNotPersistedError, UserNotFoundError
from project_manager.model import UserModel
from project_manager.services import user_service


class UserServiceCreateUserTests(unittest.TestCase):

    def test_create_user_success(self):
        def _persist_function_success_mock(user_model):
            return user_model
        create_user_dto = UserCreatedDto()
        user_created_dto = user_service.create_user(create_user_dto, _persist_function_success_mock)
        self.assertIsInstance(user_created_dto, Success)
        self.assertIsInstance(user_created_dto.unwrap(),UserCreatedDto)

    def test_create_user_fail(self):
        def _persist_function_fail_mock(user_model):
            return None
        create_user_dto = UserCreatedDto()
        user_created_dto = user_service.create_user(create_user_dto, _persist_function_fail_mock)
        self.assertIsInstance(user_created_dto, Failure)
        self.assertIsInstance(user_created_dto.failure(),UserNotPersistedError)



class userServiceGetUserByIdTests(unittest.TestCase):

    def test_get_user_by_id_success(self):
        def _find_in_db_function_success_mock(uid):
            return UserModel()

        found_user = user_service.find_user_by_id(Any,_find_in_db_function_success_mock)
        self.assertIsInstance(found_user, Success)
        self.assertIsInstance(found_user.unwrap(), UserGetDto)

    def test_get_user_by_id_fail(self):
        def _find_in_db_function_fail_mock(uid):
            return None

        found_user = user_service.find_user_by_id(Any,_find_in_db_function_fail_mock)
        self.assertIsInstance(found_user, Failure)
        self.assertIsInstance(found_user.failure(), UserNotFoundError)
