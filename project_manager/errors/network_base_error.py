from returns.result import Result, Success

from project_manager.dtos.dto_base import Dto
from project_manager.errors.base_error import Error

class NetworkError(Error):
    def __init__(self, message: str = '', status_code: int = 200):
        super().__init__(message)
        self.status_code = status_code


def manage_network_result(result: Result[Dto,NetworkError]):
    if isinstance(result, Success):
        return result.unwrap().serialize(), 200
    return result.failure().message, result.failure().status_code