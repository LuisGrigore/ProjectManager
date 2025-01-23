from flask import jsonify

from project_manager.dtos.dto_base import Dto


class TokenGetDto(Dto):
    def __init__(self, token):
        self._token = token

    def deserialize(self, data):
        '''Overwrites abstract'''
        self._token = data.get("token")


    def serialize(self):
        return jsonify({'token': self._token})

    @property
    def token(self):
        return self._token