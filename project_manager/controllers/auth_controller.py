from auth.auth_session import AuthSession


def register(app, auth_session: AuthSession):
    @app.route('/login')
    def login():
        pass
