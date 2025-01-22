from __future__ import annotations

from typing import Dict

import flask
from flask import jsonify
from project_manager.dtos.dto_base import Dto

class UserCreateDto(Dto):
    '''hola'''
    def __init__(self, name: str = None, password: str = None):
        self._name = name
        self._password = password

    @property
    def name(self):
        return self._name
    @property
    def password(self):
        return self._password

    def deserialize(self, data: Dict):
        '''Overwrites abstract'''
        self._name = data.get("name")
        self._password = data.get("password")

    def serialize(self) -> flask.Response:
        '''Overwrites abstract'''
        return jsonify({'name': self._name, 'password': self._password})

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