from auth.token_model import Token
from project_manager.dtos.token_dtos import TokenGetDto


def token_to_token_get_dto(token: Token) -> TokenGetDto:
    token_get_dto: TokenGetDto = TokenGetDto(token.__hash__())
    return token_get_dto