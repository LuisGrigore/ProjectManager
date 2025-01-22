from typing import Dict

from auth.token_model import Token

class AuthSession:
    def __init__(self, concurrent_tokens):
        self._concurrent_tokens: Dict[str, Token] = concurrent_tokens

    def add_token(self, token: Token) -> Token:
        self._concurrent_tokens[token.__hash__()] = token
        return token

    def validate_token(self, username: str, token_hash: str) -> bool:
        if self._concurrent_tokens.__contains__(token_hash):
            if self._concurrent_tokens.get(token_hash).belongs_to(username):
                return True
        return False

