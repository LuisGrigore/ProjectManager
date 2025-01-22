import unittest
from datetime import datetime, timedelta
from typing import Any

from auth.token_model import Token


class TokenTests(unittest.TestCase):
    def test_is_alive_returns_true(self):
        token: Token = Token(username=Any, ttl = 2, creation_time=datetime.now() - timedelta(minutes=1))
        self.assertTrue(token.is_alive(datetime.now()), 'Expected token to be alive')

    def test_is_alive_returns_false(self):
        token: Token = Token(username=Any, ttl = 1, creation_time=datetime.now() - timedelta(minutes=3))
        self.assertFalse(token.is_alive(datetime.now()),'Expected token to be dead')

    def test_belongs_to_returns_true(self):
        token: Token = Token(username='a', ttl = 1, creation_time=datetime.now())
        self.assertTrue(token.belongs_to('a'))

    def test_belongs_to_returns_false(self):
        token: Token = Token(username='a', ttl = 1, creation_time=datetime.now())
        self.assertFalse(token.belongs_to('b'))

    def test_hash(self):
        token1: Token = Token(username='a', ttl=1, creation_time=datetime.now())
        token2: Token = Token(username='b', ttl=1, creation_time=datetime.now())
        self.assertNotEquals(token1.__hash__(),token2.__hash__())
