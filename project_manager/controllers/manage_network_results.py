from typing import List

from returns.result import Success, Result

from project_manager.dtos.dto_base import Dto
from project_manager.errors.network_base_error import NetworkError


def manage_network_result(result: Result[Dto,NetworkError]):
    if isinstance(result, Success):
        return result.unwrap().serialize(), 200
    return result.failure().message, result.failure().status_code
