from __future__ import annotations

from project_manager.app import db

Model = db.Model


class FragmentModel(db.Model):
    __tablename__ = 'fragments'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)

    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable = False)

    @staticmethod
    def get_FragmentModel(name = None, project_id = None) -> ProjectModel:
        fragment_model = ProjectModel()
        fragment_model.name = name
        fragment_model.project_id = project_id
        return fragment_model



class ProjectModel(Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer,  primary_key = True)
    name = db.Column(db.Text, nullable = False)
    #creation_date = db.Column(db.Date, nullable = False)
    fragments = db.relationship('FragmentModel', backref='project', lazy=True)


    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @staticmethod
    def get_ProjectModel(name = None, owner_id = None) -> ProjectModel:
        project_model = ProjectModel()
        project_model.name = name
        project_model.owner_id = owner_id
        return project_model

class UserModel(Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable=False)
    projects = db.relationship('ProjectModel', backref='user', lazy=True)

    @staticmethod
    def get_UserModel(name = None, password = None) -> UserModel:
        user_model = UserModel()
        user_model.name = name
        user_model.password = password
        return user_model
