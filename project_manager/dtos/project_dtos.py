from flask import jsonify

from project_manager.dtos.dto_base import Dto


class ProjectCreateDto(Dto):
    def __init__(self, name: str = None, owner_id: int = None):
        self._name = name
        self._owner_id = owner_id

    def deserialize(self, data):
        self._name = data.get('name')
        self._owner_id = data.get('owner_id')

    def serialize(self):
        return jsonify({'name': self._name, 'owner_id': self._owner_id})

    @property
    def name(self):
        return self._name
    @property
    def owner_id(self):
        return self._owner_id


class ProjectGetDto(Dto):
    def __init__(self, name: str, owner_id: int):
        self._name = name
        self._owner_id = owner_id

    def deserialize(self, data):
        self._name = data.get('name')
        self._owner_id = data.get('owner_id')

    def serialize(self):
        return jsonify({'name': self._name, 'owner_id': self._owner_id})

    @property
    def name(self):
        return self._name
    @property
    def owner_id(self):
        return self._owner_id


class ProjectCreatedDto(Dto):
    def __init__(self, name: str, owner_id: int):
        self._name = name
        self._owner_id = owner_id

    def deserialize(self, data):
        self._name = data.get('name')
        self._owner_id = data.get('owner_id')

    def serialize(self):
        return jsonify({'name': self._name, 'owner_id': self._owner_id})

    @property
    def name(self):
        return self._name
    @property
    def owner_id(self):
        return self._owner_id