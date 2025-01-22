import unittest
from typing import Any
from unittest.mock import patch

from project_manager.model import UserModel
from project_manager.repos import user_repos


class UserReposTests(unittest.TestCase):

    @patch('project_manager.app.db.session.add')
    @patch('project_manager.app.db.session.commit')
    def test_save_user_success(self, mock_db_session_commit, mock_db_session_add):
        #create user model to save
        user = UserModel()

        #mock db behaviour
        mock_db_session_add.return_value = Any
        mock_db_session_commit.return_value = Any

        #call the function being tested
        user_repos.save_user(user)

        #assert that the right calls to the db are made
        mock_db_session_commit.assert_called_with()
        mock_db_session_add.assert_called_with(user)

    @patch('project_manager.app.db.session.add')
    @patch('project_manager.app.db.session.commit')
    def test_save_user_db_add_fail(self, mock_db_session_commit, mock_db_session_add):
        # create user model to save
        user = UserModel()

        # mock db behaviour
        mock_db_session_add.side_effect = ValueError("db error")
        mock_db_session_commit.side_effect = ValueError("db error")

        # call the function being tested
        result = user_repos.save_user(user)

        # assert that the right calls to the db are made
        mock_db_session_add.assert_called_with(user)

        self.assertEquals(result,None)

    @patch('project_manager.app.db.session.add')
    @patch('project_manager.app.db.session.commit')
    def test_save_user_db_commit_fail(self, mock_db_session_commit, mock_db_session_add):
        # create user model to save
        user = UserModel()

        # mock db behaviour
        mock_db_session_add.return_value = Any
        mock_db_session_commit.side_effect = ValueError("db error")

        # call the function being tested
        result = user_repos.save_user(user)

        # assert that the right calls to the db are made
        mock_db_session_commit.assert_called_with()
        mock_db_session_add.assert_called_with(user)
        self.assertEquals(result, None)
