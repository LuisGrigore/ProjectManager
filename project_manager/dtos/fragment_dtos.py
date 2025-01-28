from flask import jsonify, Response

from project_manager.dtos.dto_base import CreateDto, GetDto


class FragmentCreateDto(CreateDto):
    def __init__(self, name: str = None, project_id: int = None) -> object:
        self._name = name
        self._project_id = project_id

    def deserialize(self, data):
        self._name = data.get('name')
        self._project_id = data.get('project_id')

    def serialize(self) -> Response:
        return jsonify({'name': self._name, 'project_id': self._project_id})

    @property
    def name(self):
        return self._name
    @property
    def project_id(self):
        return self._project_id


class FragmentGetDto(GetDto):
    def __init__(self, name: str = None, project_id: int = None):
        self._name = name
        self._project_id = project_id

    def deserialize(self, data):
        self._name = data.get('name')
        self._project_id = data.get('project_id')

    def serialize(self) -> Response:
        return jsonify({'name': self._name, 'project_id': self._project_id})

    @property
    def name(self):
        return self._name
    @property
    def project_id(self):
        return self._project_id
