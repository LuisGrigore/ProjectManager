from typing import Dict

from auth.token_model import Token

class AuthSession:
    def __init__(self, current_tokens: Dict[str, Token]):
        self._current_tokens: Dict[str, Token] = current_tokens

    def add_token(self, token: Token) -> Token:
        self._current_tokens[token.__hash__()] = token
        return token

    def validate_token(self, username: str, token_hash: str) -> bool:
        if self._current_tokens.__contains__(token_hash):
            if self._current_tokens.get(token_hash).belongs_to(username):
                return True
        return False

    @property
    def current_tokens(self):
        return self._current_tokens.copy()