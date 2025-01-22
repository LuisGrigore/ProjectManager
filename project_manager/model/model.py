from __future__ import annotations

from project_manager.app import db

'''
class FragmentModel(db.Model):
    __tablename__ = 'fragments'
    id = db.Column(db.Integer, primary_key = True)
    owner = db.relationship('User', back_populates='projects')
    fragments = db.relationship('Fragment', back_populates='projects')
    assigned_to = db.relationship('User', back_populates ='fregments', uselist = False)
    name= db.Column(db.Text, nullable=False)


class ProjectModel(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer,  primary_key = True)
    meta_data = db.relationship('ProjectMetadata', back_populates ='project', uselist = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    owner = db.relationship('User', back_populates='projects')
    fragments = db.relationship('Fragment', back_populates ='projects')
    name = db.Column(db.Text, nullable = False)
    creation_date = db.Column(db.Date, nullable = False)
'''
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable=False)
    #projects = db.relationship('Project', back_populates ='users')

    @staticmethod
    def get_UserModel(name = None) -> UserModel:
        user_model = UserModel()
        user_model.name = name
        return user_model
        #self.projects = []