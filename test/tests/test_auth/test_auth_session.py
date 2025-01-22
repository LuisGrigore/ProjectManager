import unittest
from datetime import datetime
from typing import Any

from auth.auth_session import AuthSession
from auth.token_model import Token


class AuthSessionTests(unittest.TestCase):
    def test_add_token(self):
        auth_session: AuthSession = AuthSession({})
        token: Token = Token(username=Any, ttl=1, creation_time= datetime.now())
        self.assertEqual(auth_session.add_token(token), token)
        self.assertEqual(auth_session.current_tokens.get(token.__hash__()), token)

    def test_validate_token_returns_true(self):
        auth_session: AuthSession = AuthSession({})
        username: str = 'a'
        token: Token = Token(username=username, ttl=1, creation_time=datetime.now())
        auth_session.add_token(token)
        self.assertTrue(auth_session.validate_token(username,token.__hash__()))

    def test_validate_token_returns_false(self):
        auth_session: AuthSession = AuthSession({})
        username: str = 'a'
        token: Token = Token(username=username, ttl=1, creation_time=datetime.now())
        auth_session.add_token(token)
        self.assertFalse(auth_session.validate_token(Any,token.__hash__()))
        self.assertFalse(auth_session.validate_token(username, Any))
        self.assertFalse(auth_session.validate_token(Any, Any))