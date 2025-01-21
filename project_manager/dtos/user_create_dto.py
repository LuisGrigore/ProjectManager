from __future__ import annotations

from typing import Dict

from flask import jsonify

from project_manager.dtos.dto_base import Dto


class UserCreateDto(Dto):
    def __init__(self, name: str = None):
        self.name = name
    def deserialize(self, data: Dict):
        self.name = data.get("name")

    def serialize(self):
        return jsonify({'name': self.name})

class UserCreatedDto(Dto):
    def __init__(self, name: str = None):
        self.name = name

    def deserialize(self, data: Dict):
        self.name = data.get("name")

    def serialize(self):
        return jsonify({'name': self.name})

class UserGetDto(Dto):
    def __init__(self, name: str = None):
        self.name = name

    @staticmethod
    def serialize(user_get_dto: UserGetDto):
        return jsonify({'name': user_get_dto.name})