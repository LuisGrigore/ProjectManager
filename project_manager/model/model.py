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

'''
class ProjectModel(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer,  primary_key = True)
    name = db.Column(db.Text, nullable = False)

    owner = db.relationship('UserModel', back_populates='projects')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    creation_date = db.Column(db.Date, nullable = False)

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable = False)
    password = db.Column(db.Text, nullable=False)
    projects = db.relationship('ProjectModel', back_populates = 'owner')

    @staticmethod
    def get_UserModel(name = None, password = None) -> UserModel:
        user_model = UserModel()
        user_model.name = name
        user_model.password = password
        return user_model
        #self.projects = []