from __future__ import annotations

from typing import Dict
from flask import jsonify
from project_manager.dtos.dto_base import Dto

class UserCreateDto(Dto):
    '''hola'''
    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self):
        return self._name

    def deserialize(self, data: Dict):
        '''Overwrites abstract'''
        self._name = data.get("name")

    def serialize(self):
        '''Overwrites abstract'''
        return jsonify({'name': self._name})

class UserCreatedDto(Dto):
    '''hoola'''
    def __init__(self, name: str = None):
        self._name = name

    @property
    def name(self):
        return self._name

    def deserialize(self, data: Dict):
        '''Overwrites abstract'''
        self._name = data.get("name")

    def serialize(self):
        '''Overwrites abstract'''
        return jsonify({'name': self._name})

class UserGetDto(Dto):
    '''hola'''
    def __init__(self, name: str = None):
        self.name = name

    @staticmethod
    def serialize(user_get_dto: UserGetDto):
        return jsonify({'name': user_get_dto.name})